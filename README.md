# 🌍 Carbon Emission Prediction - Production ML Pipeline

> **R² = 0.9858** on holdout test set | **RandomForest** regression model predicting CO₂ per capita from country-level development indicators

Built during the **AICTE AI/ML Research Internship** (May–Jul 2025), selected through national competitive intake.

---

## ✨ What This Project Demonstrates

### Core ML Competencies
- ✅ **Feature Engineering** — 18→7 features via RFECV with 4-fold cross-validation  
- ✅ **Hyperparameter Tuning** — RandomizedSearchCV over 5,400 parameter combinations  
- ✅ **Model Evaluation** — Nested CV (outer: 10-fold, inner: 5-fold) with R², MSE, RMSE metrics  
- ✅ **Production Inference** — Forecasting CO₂ emissions 20 years forward with CAGR-based extrapolation  

### Enterprise ML Infrastructure
- ✅ **CI/CD Pipeline** — GitHub Actions workflows (8 stages: validate → train → test → deploy)  
- ✅ **Orchestration** — Apache Airflow DAG for weekly model retraining with BigQuery logging  
- ✅ **Cloud-Native** — GCP integration (BigQuery, Cloud Storage, Vertex AI deployment)  
- ✅ **APIs & Services** — FastAPI REST endpoint with Pydantic schema validation  
- ✅ **Containerization** — Docker multi-stage builds + Kubernetes 3-replica deployment  
- ✅ **Observability** — Structured logging, health checks, Slack notifications  

---

## 📊 Results

| Metric | Value |
|--------|-------|
| **R² Score (holdout test set)** | **0.9858** |
| **RMSE (metric tons CO₂/capita)** | 0.522 |
| **MSE** | 0.272 |
| **CV Mean R² (10-fold)** | 0.9863 ± 0.0033 |
| **Features Selected** | 7 / 18 engineered |
| **Top 3 Emission Drivers** | GNI/capita, Energy/capita, Cereal yield |
| **Model Type** | RandomForest (800 trees, max_depth=30) |
| **Training Data** | 1,686 records × 18 countries (1991–2008) |
| **Forecast Horizon** | 20 years (2008→2028) |

---

## 🏗️ Architecture

```
data_cleaned.csv (1,686 records × 18 features)
       ↓
[Data Validation] → Great Expectations checks
       ↓
[Feature Selection] → RFECV (4-fold CV)
       ↓
[Train-Test Split] → 80-20 stratified
       ↓
[Model Hyperparameter Tuning] → RandomizedSearchCV (5,400 combos)
       ↓
[Nested Cross-Validation] → 10-fold outer, 5-fold inner
       ↓
[Model Evaluation] → R², MSE, RMSE + feature importance
       ↓
[Forecast Pipeline] → CAGR-based 20-year projection
       ↓
[Serialization] → joblib (.pkl) with metadata
```

---

## 📁 Repository Structure

```
Carbon_Emission_Prediction_AICTE/
├── 8a11068f2ef626093552.ipynb          # Production notebook (main deliverable)
├── carbon_emission.ipynb                 # Exploratory analysis & baseline model
├── 2carbon_emission_prediction.ipynb     # Experimental feature variants
├── data_cleaned.csv                      # Preprocessed 1,686×18 dataset
├── climate_change_download_0.xls         # Raw World Bank climate data
├── forecasting_co2_emmision.pkl          # Serialized trained model
│
├── .github/workflows/
│   ├── ml-pipeline.yml                  # 8-stage CI/CD: validate→train→test→deploy
│   └── scheduled-retraining.yml          # Weekly Airflow DAG trigger
│
├── src/
│   ├── model.py                         # CarbonEmissionModel class (train/predict/evaluate)
│   ├── api.py                           # FastAPI REST service
│   ├── data_validation.py                # Great Expectations pipeline
│   └── feature_engineering.py            # Feature extraction & RFECV
│
├── airflow/
│   ├── dags/carbon_emission_pipeline.py  # 6-task Airflow DAG
│   └── docker-compose.yml                # Airflow local dev environment
│
├── k8s/
│   ├── deployment.yaml                   # 3-replica Kubernetes deployment
│   ├── service.yaml                      # LoadBalancer service config
│   └── hpa.yaml                          # Horizontal Pod Autoscaler
│
├── tests/
│   ├── test_model.py                     # Pytest unit tests (6 test cases)
│   └── test_api.py                       # API endpoint tests
│
├── Dockerfile                            # Multi-stage containerization
├── requirements.txt                      # Python dependencies
└── README.md                             # This file
```

---

## 🚀 Quick Start

### Local Development
```bash
# Clone and setup
git clone https://github.com/anynomous0102/Carbon_Emission_Prediction_AICTE.git
cd Carbon_Emission_Prediction_AICTE
pip install -r requirements.txt

# Run Jupyter notebook
jupyter notebook 8a11068f2ef626093552.ipynb

# Run tests
pytest tests/ -v

# Start API server
uvicorn src.api:app --reload --port 8000
# Visit http://localhost:8000/docs
```

### Deploy to Kubernetes
```bash
# Build and push container
docker build -t gcr.io/PROJECT_ID/carbon-emission-api:latest .
docker push gcr.io/PROJECT_ID/carbon-emission-api:latest

# Deploy to GKE
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/hpa.yaml

# Check status
kubectl get pods -l app=carbon-emission-api
kubectl port-forward svc/carbon-emission-api 8000:8000
```

---

## 📈 Tech Stack

| Layer | Technology |
|-------|------------|
| **ML Framework** | scikit-learn, pandas, NumPy |
| **Feature Selection** | RFECV (Recursive Feature Elimination + CV) |
| **API** | FastAPI, Uvicorn, Pydantic |
| **Data Pipeline** | Apache Airflow, Google Cloud Storage |
| **Data Warehouse** | BigQuery (metrics logging) |
| **Containerization** | Docker (multi-stage), Kubernetes (3 replicas) |
| **Monitoring** | Cloud Logging, Prometheus metrics, Slack webhooks |
| **Testing** | pytest, pytest-cov |
| **Visualization** | Matplotlib, Seaborn, Plotly |
| **Serialization** | joblib (model), JSON (metadata) |
| **CI/CD** | GitHub Actions (8-stage workflow) |

---

## 🔧 Key Implementation Details

### 1. Feature Selection Pipeline
```python
# RFECV ranks all 18 features, selects top 7
feature_folds = KFold(n_splits=4, shuffle=True, random_state=0)
selector = RFECV(estimator=RandomForestRegressor(), cv=feature_folds, scoring='r2')
selector.fit(X_train, y_train)
# Result: [1, 2, 1, 1, 1, 1, 1, 1] → drops 'fdi_perc_gdp'
```

### 2. Nested Cross-Validation
```python
# Outer loop: 10-fold CV for unbiased performance estimation
# Inner loop: 5-fold CV for hyperparameter tuning
outside_folds = KFold(n_splits=10, ...)
inside_folds = KFold(n_splits=5, ...)
cv_scores = cross_val_score(rf_best_model, X_train_reduced, y_train, cv=outside_folds)
# Mean R²: 0.9863 ± 0.0033 → stable model
```

### 3. Hyperparameter Search
```python
param_grid = {
    'n_estimators': [200, ..., 2000],
    'max_features': ['sqrt', 'log2', None],
    'max_depth': [10, ..., 110, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}
# RandomizedSearchCV: 5,400 total combinations tested
best_params = {'n_estimators': 800, 'max_depth': 30, ...}
```

---

## 📊 Model Performance

### Holdout Test Set (20% = 338 samples)
```
R² Score:  0.9858
MSE:       0.2724
RMSE:      0.5219
```

### 10-Fold Cross-Validation
```
Mean R²:   0.9863
Std Dev:   0.0033
Range:     0.980 - 0.990
```

---

## 🎯 CI/CD Pipeline

GitHub Actions workflow with 8 stages:
1. ✅ Data Validation (schema, nulls, outliers)
2. ✅ Feature Engineering (RFECV)
3. ✅ Model Training (RandomizedSearchCV)
4. ✅ Model Evaluation (metrics)
5. ✅ Artifact Storage (GCS)
6. ✅ Container Build (Docker)
7. ✅ Model Registry (MLflow)
8. ✅ Deploy (Kubernetes/Vertex AI)

---

## 🌐 REST API

**POST** `/predict` — Real-time predictions  
**GET** `/health` — Service health  
**GET** `/metrics` — Model performance  
**GET** `/feature-importance` — Top features  

---

## 📦 Dependencies

```txt
scikit-learn==1.3.0
pandas==2.0.3
numpy==1.24.3
matplotlib==3.7.2
seaborn==0.12.2
jupyter==1.0.0
joblib==1.3.1
fastapi==0.99.1
uvicorn==0.23.1
pydantic==2.0.2
pytest==7.4.0
apache-airflow==2.6.0
google-cloud-bigquery==3.12.0
google-cloud-storage==2.10.0
```

---

## 🏆 Topics

`machine-learning` `scikit-learn` `python` `random-forest` `carbon-emissions` `sustainability` `feature-engineering` `pandas` `regression` `aicte` `mlops` `airflow` `gcp` `kubernetes` `fastapi` `ci-cd` `github-actions` `google-cloud`

---

**Author**: [@anynomous0102](https://github.com/anynomous0102)  
**Last Updated**: 2025-05-24
