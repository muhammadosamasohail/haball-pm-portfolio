"""Generates synthetic distributor order/payment history for the prototype.

All data here is fabricated for demonstration. Nothing in this module reads
from or represents any real Haball system or real distributor.
"""
from __future__ import annotations

import random
from datetime import date, timedelta

DISTRIBUTOR_PROFILES = {
    "DST-04821": {
        "name": "Karachi Traders Pvt Ltd",
        "months": 12,
        "order_interval_days": (18, 4),   # (mean, stddev) -> fairly steady
        "order_value_pkr": (85000, 12000),
        "on_time_rate": 0.88,
        "volume_trend_pct_per_month": 2.0,  # rising
        "wasal_digitized": False,
        "sparse_recent_quarter": True,
    },
    "DST-01190": {
        "name": "Al-Fateh Distribution",
        "months": 12,
        "order_interval_days": (14, 2),   # very steady
        "order_value_pkr": (140000, 9000),
        "on_time_rate": 0.97,
        "volume_trend_pct_per_month": 3.5,
        "wasal_digitized": True,
        "sparse_recent_quarter": False,
    },
    "DST-07734": {
        "name": "Sindh Agro Supplies",
        "months": 12,
        "order_interval_days": (30, 18),  # irregular
        "order_value_pkr": (60000, 9000),
        "on_time_rate": 0.61,
        "volume_trend_pct_per_month": -6.0,  # declining
        "wasal_digitized": False,
        "sparse_recent_quarter": True,
    },
    "DST-09902": {
        "name": "New Horizon Retail Co",
        "months": 3,
        "order_interval_days": (20, 6),
        "order_value_pkr": (50000, 15000),
        "on_time_rate": 0.90,
        "volume_trend_pct_per_month": 1.0,
        "wasal_digitized": False,
        "sparse_recent_quarter": True,
    },
}


def list_distributor_ids() -> list[str]:
    return list(DISTRIBUTOR_PROFILES.keys())


def generate_history(distributor_id: str, seed: int = 42) -> dict:
    """Returns a dict with 'orders' and 'payments' event lists for the distributor."""
    profile = DISTRIBUTOR_PROFILES[distributor_id]
    rng = random.Random(seed + sum(ord(c) for c in distributor_id))

    end = date.today()
    start = end - timedelta(days=30 * profile["months"])

    mean_interval, std_interval = profile["order_interval_days"]
    mean_value, std_value = profile["order_value_pkr"]

    orders = []
    current = start
    month_index = 0
    while current < end:
        interval = max(3, int(rng.gauss(mean_interval, std_interval)))
        current = current + timedelta(days=interval)
        if current >= end:
            break
        elapsed_months = (current - start).days / 30
        trend_multiplier = 1 + (profile["volume_trend_pct_per_month"] / 100) * elapsed_months
        value = max(5000, rng.gauss(mean_value, std_value) * trend_multiplier)
        orders.append({"date": current, "value_pkr": round(value, -2)})

    payments = []
    for order in orders:
        due = order["date"] + timedelta(days=15)
        is_late_quarter = profile["sparse_recent_quarter"] and (end - order["date"]).days < 90
        on_time_chance = profile["on_time_rate"] * (0.6 if is_late_quarter else 1.0)
        on_time = rng.random() < on_time_chance
        settled = due if on_time else due + timedelta(days=rng.randint(1, 20))
        payments.append({
            "order_date": order["date"],
            "due_date": due,
            "settled_date": settled,
            "on_time": on_time,
        })

    return {
        "distributor_id": distributor_id,
        "name": profile["name"],
        "window_months": profile["months"],
        "orders": orders,
        "payments": payments,
        "wasal_digitized": profile["wasal_digitized"],
    }
