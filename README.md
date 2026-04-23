# Superstore Sales Intelligence — Business Analysis Dashboard

## Overview
A business intelligence analysis of 4 years of retail sales data (2014–2017)
identifying profit leakage, loss-making areas, and actionable recommendations
for a $2.29M revenue superstore.

## Key Findings

### 1. Discounts Above 20% Are Loss-Making
| Discount Range | Avg Profit Margin | Status |
|---------------|------------------|--------|
| 0–10% | +33.7% | ✅ Profitable |
| 10–20% | +17.5% | ✅ Profitable |
| 20–30% | -11.6% | 🚨 Loss |
| 40–50% | -53.6% | 🚨 Loss |
| 50–80% | -113.9% | 💀 Severe Loss |

### 2. Furniture Category Is Broken
- $742k in sales but only $18k profit (2.5% margin)
- Tables sub-category alone: **-$17,725 net loss**
- Root cause: 26% average discount on Tables

### 3. Central Region Needs Intervention
- Only region with **negative profit margin (-10.4%)**
- Average discount of 24% vs 11–15% in other regions

### 4. Business Growing But Not Improving
- Orders grew 66% from 2014 to 2017
- Profit margin stuck at ~12% all 4 years
- Growth is volume-driven, not efficiency-driven

## Business Recommendations
| Priority | Action | Expected Impact |
|----------|--------|----------------|
| HIGH | Cap all discounts at 20% | Eliminate loss-making orders |
| HIGH | Audit Central region discounts | Fix -10.4% margin |
| MEDIUM | Review Tables and Bookcases pricing | Stop -$17k annual loss |
| MEDIUM | Increase Technology investment | Highest margin at 15.6% |
| LOW | Run Q1 promotions (Jan–Feb) | Reduce seasonal revenue dip |

## Tech Stack
- Python (Pandas, NumPy)
- Matplotlib, Seaborn
- Streamlit (deployed dashboard)

## Dataset
Sample Superstore Sales Dataset — 9,994 orders across 4 years

## Project Structure
superstore-sales-analysis/

├── data/                        # Dataset

├── superstore_analysis.ipynb    # Full analysis notebook

└── app.py                       # Streamlit dashboard

## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Author
**Piyush Kumar** — Mechanical Engineering, IIT Goa
