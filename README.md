 Carbon Emission Prediction

> **R² = 0.92** on holdout test set — gradient-boosted regression model predicting industrial carbon emissions from raw sensor data.

Built during the AICTE AI/ML Research Internship (May–Jul 2025), selected through national competitive intake.

---------------------------------------------------------------------------------------------------------------

## What this does

Predicts CO₂ emission levels from industrial processes using 15+ engineered features extracted from raw sensor readings. The model identifies the **top 3 emission drivers** via permutation-based feature importance — giving actionable, data-backed reduction targets rather than just a prediction score.

---------------------------------------------------------------------------------------------------------------

## Results

| Metric | Value |
|--------|-------|
| R² score (holdout test set) | **0.92** |
| Features engineered | 15+ |
| Top emission drivers identified | 3 |
| Model type | Gradient-boosted regression |

---------------------------------------------------------------------------------------------------------------

## Tech stack

- Python · scikit-learn · Pandas · NumPy · Matplotlib
- Jupyter Notebook

---------------------------------------------------------------------------------------------------------------

## Files

| File | Description |
|------|-------------|
| `carbon_emission.ipynb` | Main model notebook — data cleaning, feature engineering, training, evaluation |
| `2carbon_emission_prediction.ipynb` | Experimental version with alternate feature sets |
| `data_cleaned.csv` | Preprocessed dataset used for training |
| `climate_change_download_0.xls` | Raw source data |

---------------------------------------------------------------------------------------------------------------

## How to run

```bash
pip install scikit-learn pandas numpy matplotlib jupyter
jupyter notebook carbon_emission.ipynb
```

---------------------------------------------------------------------------------------------------------------

## Context

This project was developed as part of the **AICTE National AI/ML Internship Program** (May–July 2025). The goal was to build a production-quality regression pipeline — not just a model — with proper train/test splitting, feature importance analysis, and interpretable outputs that could inform real industrial decisions.

The evaluation methodology was designed to align with published ML benchmarking standards, including permutation-based importance scoring rather than impurity-based alternatives, which can be misleading on high-cardinality features.

---------------------------------------------------------------------------------------------------------------

## Topics

`machine-learning` `scikit-learn` `python` `gradient-boosting` `carbon-emissions` `sustainability` `feature-engineering` `pandas` `regression` `aicte`
