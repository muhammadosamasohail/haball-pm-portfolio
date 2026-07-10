"""Rules-based signal engine.

Deliberately simple arithmetic, no trained model, no accuracy claim, no
default prediction. Every value here is inspectable: it is a plain
statistic computed from the mock order/payment history, nothing more.
See ../../SRS_underwriting_signals.md (FR1-FR9) for the requirements
this implements.
"""
from __future__ import annotations

import statistics
from datetime import date

MIN_ORDERS_FOR_CONSISTENCY = 6
MIN_PAYMENTS_FOR_TIMELINESS = 10
MIN_ORDERS_FOR_TREND = 6


def _coefficient_of_variation(values: list[float]) -> float | None:
    if len(values) < 2:
        return None
    mean = statistics.mean(values)
    if mean == 0:
        return None
    stdev = statistics.pstdev(values)
    return stdev / mean


def order_consistency(orders: list[dict]) -> dict:
    """FR1: coefficient of variation of order intervals. Lower = steadier."""
    if len(orders) < MIN_ORDERS_FOR_CONSISTENCY:
        return {"available": False, "observations": len(orders), "reason": "insufficient order history"}

    sorted_orders = sorted(orders, key=lambda o: o["date"])
    intervals = [
        (sorted_orders[i]["date"] - sorted_orders[i - 1]["date"]).days
        for i in range(1, len(sorted_orders))
    ]
    cv = _coefficient_of_variation(intervals)
    if cv is None:
        return {"available": False, "observations": len(orders), "reason": "insufficient variation to compute"}

    if cv < 0.25:
        label = "Steady"
    elif cv < 0.5:
        label = "Somewhat variable"
    else:
        label = "Irregular"

    return {
        "available": True,
        "value_label": f"{label} (CV {cv:.2f})",
        "observations": len(orders),
        "source": "Blink",
        "explain": "How regular this distributor's orders are. Lower variation means steadier ordering.",
    }


def payment_timeliness(payments: list[dict]) -> dict:
    """FR2: share of payments settled on or before their due date."""
    if len(payments) < MIN_PAYMENTS_FOR_TIMELINESS:
        return {"available": False, "observations": len(payments), "reason": "insufficient payment history"}

    on_time = sum(1 for p in payments if p["on_time"])
    rate = on_time / len(payments)

    return {
        "available": True,
        "value_label": f"{rate * 100:.0f}% on time",
        "observations": len(payments),
        "source": "Blink",
        "explain": "Share of payments made on or before the due date.",
    }


def volume_trend(orders: list[dict]) -> dict:
    """FR3: slope of order volume over the window, expressed as % per quarter."""
    if len(orders) < MIN_ORDERS_FOR_TREND:
        return {"available": False, "observations": len(orders), "reason": "insufficient order history"}

    sorted_orders = sorted(orders, key=lambda o: o["date"])
    first_date = sorted_orders[0]["date"]
    xs = [(o["date"] - first_date).days for o in sorted_orders]
    ys = [o["value_pkr"] for o in sorted_orders]

    n = len(xs)
    mean_x = sum(xs) / n
    mean_y = sum(ys) / n
    numerator = sum((xs[i] - mean_x) * (ys[i] - mean_y) for i in range(n))
    denominator = sum((xs[i] - mean_x) ** 2 for i in range(n))
    if denominator == 0 or mean_y == 0:
        return {"available": False, "observations": len(orders), "reason": "insufficient variation to compute"}

    daily_slope = numerator / denominator
    pct_per_quarter = (daily_slope * 90 / mean_y) * 100

    if pct_per_quarter > 1:
        direction = "Rising"
    elif pct_per_quarter < -1:
        direction = "Declining"
    else:
        direction = "Flat"

    return {
        "available": True,
        "value_label": f"{direction} ({pct_per_quarter:+.1f}% / qtr)",
        "observations": len(orders),
        "source": "Blink, corroborated by Wasal" if pct_per_quarter else "Blink",
        "explain": "Direction of order volume over the window: rising, flat, or declining.",
    }


def data_gaps(history: dict, order_result: dict, payment_result: dict, trend_result: dict) -> list[str]:
    """FR6: plain-language gap notes, shown instead of silently guessing."""
    gaps = []
    if not history["wasal_digitized"]:
        gaps.append("No Wasal invoice history found. Order-volume trend cannot be corroborated by invoices.")
    if not order_result["available"]:
        gaps.append(f"Order consistency unavailable: {order_result['reason']} ({order_result['observations']} orders on file).")
    if not payment_result["available"]:
        gaps.append(f"Payment timeliness unavailable: {payment_result['reason']} ({payment_result['observations']} payments on file).")
    if not trend_result["available"]:
        gaps.append(f"Order-volume trend unavailable: {trend_result['reason']} ({trend_result['observations']} orders on file).")

    return gaps


def illustrative_tier(order_result: dict, payment_result: dict, trend_result: dict) -> str:
    """FR7: non-binding tier label. Illustrative only, not a decision."""
    available_count = sum([order_result["available"], payment_result["available"], trend_result["available"]])
    if available_count == 3:
        return "Sufficient signal, standard review"
    if available_count >= 1:
        return "Partial signal, closer review"
    return "Thin file, needs manual review"


def compute_signal_profile(history: dict) -> dict:
    """Runs all signals for one distributor's history and returns a display-ready dict."""
    order_result = order_consistency(history["orders"])
    payment_result = payment_timeliness(history["payments"])
    trend_result = volume_trend(history["orders"])

    gaps = data_gaps(history, order_result, payment_result, trend_result)

    recent_cutoff_days = 90
    recent_payments = [
        p for p in history["payments"]
        if (date.today() - p["due_date"]).days <= recent_cutoff_days
    ]
    if recent_payments and len(recent_payments) < 10:
        gaps.append(
            f"Payment timeliness based on {len(recent_payments)} payments in the most recent quarter, "
            "below the recommended minimum. Treat as low-confidence for that period."
        )

    tier = illustrative_tier(order_result, payment_result, trend_result)

    return {
        "distributor_id": history["distributor_id"],
        "name": history["name"],
        "window_months": history["window_months"],
        "order_count": len(history["orders"]),
        "payment_count": len(history["payments"]),
        "wasal_digitized": history["wasal_digitized"],
        "order_consistency": order_result,
        "payment_timeliness": payment_result,
        "volume_trend": trend_result,
        "gaps": gaps,
        "tier": tier,
    }
