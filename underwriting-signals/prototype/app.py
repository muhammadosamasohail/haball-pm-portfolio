"""Wisaaq Alternative-Signal Underwriting, Streamlit prototype.

This is a work sample, not a production tool and not a claim about how
Haball's systems actually work. All distributor data is synthetic
(see data/mock_distributors.py). The signal engine is plain, rules-based
arithmetic (see signals/engine.py), not a trained model. It does not
predict default, produce an accuracy figure, or render an approve/deny
decision. It visualizes decision-support inputs for a hypothetical
credit officer reviewing a Wisaaq financing request.
"""
from __future__ import annotations

import streamlit as st

from data.mock_distributors import DISTRIBUTOR_PROFILES, generate_history, list_distributor_ids
from signals.engine import compute_signal_profile

st.set_page_config(page_title="Wisaaq Signal Profile (Prototype)", page_icon="\U0001F4CB", layout="wide")

TIER_STYLE = {
    "Sufficient signal, standard review": ("#0F8A5F", "#EAF7F0"),
    "Partial signal, closer review": ("#B5850C", "#FFF7E5"),
    "Thin file, needs manual review": ("#9A5B00", "#FFF4E5"),
}


def render_metric_card(title: str, result: dict):
    with st.container(border=True):
        st.markdown(f"**{title.upper()}**")
        if result["available"]:
            st.markdown(f"### {result['value_label']}")
            st.caption(result["explain"])
            st.markdown(f"`{result['source']}`")
            st.caption(f"Based on {result['observations']} observations.")
        else:
            st.markdown("### Insufficient data")
            st.caption(f"{result['reason'].capitalize()} ({result['observations']} on file).")


st.title("Distributor Signal Profile")
st.caption(
    "Decision-support view for a hypothetical credit officer reviewing a Wisaaq financing request. "
    "Not an automated decision. Full documentation: BRD, SRS, user stories, process flow, and wireframe "
    "spec live alongside this prototype in the repo."
)

with st.sidebar:
    st.markdown("### Select a mock distributor")
    dist_id = st.selectbox(
        "Distributor",
        options=list_distributor_ids(),
        format_func=lambda d: f"{d}, {DISTRIBUTOR_PROFILES[d]['name']}",
    )
    st.divider()
    st.caption(
        "All data below is synthetic, generated for this prototype. It does not represent any real "
        "Haball distributor, and none of it is read from a real Haball system."
    )
    st.divider()
    st.markdown("**What this is not:**")
    st.caption("Not a trained model. No accuracy figure. No default prediction. No approve/deny output.")

history = generate_history(dist_id)
profile = compute_signal_profile(history)

st.divider()

header_col, tier_col = st.columns([3, 2])
with header_col:
    st.subheader(profile["name"])
    st.caption(f"Distributor ID: {profile['distributor_id']}")
with tier_col:
    color, bg = TIER_STYLE.get(profile["tier"], ("#6B7280", "#F0F2F4"))
    st.markdown(
        f"""<div style="text-align:right;">
        <span style="background:{bg}; color:{color}; font-weight:700; font-size:13px;
        padding:6px 12px; border-radius:6px; border:1px solid {color}33;">{profile['tier']}</span>
        <div style="font-size:10.5px; color:#9A9FA6; margin-top:4px;">Illustrative only. Not a rating or a decision.</div>
        </div>""",
        unsafe_allow_html=True,
    )

c1, c2, c3 = st.columns(3)
with c1:
    st.caption(f"Data window: **Last {profile['window_months']} months**")
with c2:
    st.caption(f"Observations: **{profile['order_count']} orders, {profile['payment_count']} payments**")
with c3:
    sources = "Blink, Wasal" if profile["wasal_digitized"] else "Blink only"
    st.caption(f"Sources active: **{sources}**")

st.markdown("#### Signal Metrics")
m1, m2, m3 = st.columns(3)
with m1:
    render_metric_card("Order Consistency", profile["order_consistency"])
with m2:
    render_metric_card("Payment Timeliness", profile["payment_timeliness"])
with m3:
    render_metric_card("Order-Volume Trend", profile["volume_trend"])

if profile["gaps"]:
    st.markdown("#### Data gaps")
    with st.container(border=True):
        for gap in profile["gaps"]:
            st.markdown(f"- {gap}")

st.divider()
st.caption(
    "This screen presents behavioral signals to support a credit officer's judgment. "
    "It does not underwrite, score, or approve. Figures shown are illustrative."
)

with st.expander("Signal Sources reference"):
    st.markdown(
        """
| Signal | Source product | What it draws on |
|---|---|---|
| Order consistency | Blink | Order timestamps and values |
| Payment timeliness | Blink | Payment due vs. settled dates |
| Order-volume trend | Blink (+ Wasal) | Order volume over time, corroborated by invoices |
| Digitization confirmed | Wasal | Invoice records and FBR registration status |
"""
    )
    st.caption(
        "Blink and Wasal generate the behavioral data. The Signal Engine reads it. Wisaaq's credit "
        "officer uses it. The more a distributor transacts and invoices on Haball's rails, the more "
        "underwritable they become."
    )
