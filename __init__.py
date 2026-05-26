# Customer Segmentation with K-Means

## Overview
Generates customer income/spending data, scales it, trains K-Means, saves clusters and plots.

## Why this project belongs in a data portfolio
- Shows practical data generation, cleaning, modelling and evaluation.
- Saves outputs that can be discussed on GitHub or LinkedIn.
- Uses a reproducible script structure with `src/`, `data/`, and `outputs/`.

## Tech stack
Python, pandas, NumPy, scikit-learn, matplotlib/scipy/streamlit where needed.

## How to run
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
python cluster_customers.py
```

For the Streamlit dashboard project, run:
```bash
streamlit run cluster_customers.py
```

## Expected output
The script prints evaluation results and saves generated CSV files to `data/`. Some projects also save plots to `outputs/`.
