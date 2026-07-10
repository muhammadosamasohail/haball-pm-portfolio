# Prototype: Wisaaq Signal Profile

A Streamlit app that visualizes rules-based behavioral signals for a mock distributor, as decision support for a hypothetical credit officer reviewing a Wisaaq financing request.

**What this is not:** not a trained model, no accuracy figure, no default prediction, no approve/deny output, no connection to any real Haball system or real distributor data. See the SRS's "Out of Scope" section for the full list.

## Running locally

```bash
cd underwriting-signals/prototype
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Opens at `http://localhost:8501`. Pick a mock distributor from the sidebar to see its signal profile.

## Structure

- `app.py`, the Streamlit UI
- `signals/engine.py`, the rules-based signal computations (order consistency, payment timeliness, order-volume trend), each documented against the SRS's functional requirements
- `data/mock_distributors.py`, synthetic distributor order/payment history generator, no real data

## Stack

Python, Streamlit, standard library statistics only (no ML libraries used, intentionally)
