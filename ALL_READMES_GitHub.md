# ============================================================
# README 1 — Carbon_Emission_Prediction_AICTE
# Go to that repo → click README.md → edit → paste this → commit
# ============================================================

# Carbon Emission Prediction

> **R² = 0.92** on holdout test set — gradient-boosted regression model predicting industrial carbon emissions from raw sensor data.

Built during the AICTE AI/ML Research Internship (May–Jul 2025), selected through national competitive intake.

---

## What this does

Predicts CO₂ emission levels from industrial processes using 15+ engineered features extracted from raw sensor readings. The model identifies the **top 3 emission drivers** via permutation-based feature importance — giving actionable, data-backed reduction targets rather than just a prediction score.

---

## Results

| Metric | Value |
|--------|-------|
| R² score (holdout test set) | **0.92** |
| Features engineered | 15+ |
| Top emission drivers identified | 3 |
| Model type | Gradient-boosted regression |

---

## Tech stack

- Python · scikit-learn · Pandas · NumPy · Matplotlib
- Jupyter Notebook

---

## Files

| File | Description |
|------|-------------|
| `carbon_emission.ipynb` | Main model notebook — data cleaning, feature engineering, training, evaluation |
| `2carbon_emission_prediction.ipynb` | Experimental version with alternate feature sets |
| `data_cleaned.csv` | Preprocessed dataset used for training |
| `climate_change_download_0.xls` | Raw source data |

---

## How to run

```bash
pip install scikit-learn pandas numpy matplotlib jupyter
jupyter notebook carbon_emission.ipynb
```

---

## Context

This project was developed as part of the **AICTE National AI/ML Internship Program** (May–July 2025). The goal was to build a production-quality regression pipeline — not just a model — with proper train/test splitting, feature importance analysis, and interpretable outputs that could inform real industrial decisions.

The evaluation methodology was designed to align with published ML benchmarking standards, including permutation-based importance scoring rather than impurity-based alternatives, which can be misleading on high-cardinality features.

---

## Topics

`machine-learning` `scikit-learn` `python` `gradient-boosting` `carbon-emissions` `sustainability` `feature-engineering` `pandas` `regression` `aicte`


# ============================================================
# README 2 — breast_cancer_prediction-
# Go to that repo → click README.md → edit → paste this → commit
# ============================================================

# Breast Cancer Detection

> Binary ML classifier for early-stage breast cancer detection — reduced feature dimensionality from **30 → 15** and tuned decision threshold to minimise false negatives.

---

## What this does

Builds a binary classifier on the **Wisconsin Diagnostic Breast Cancer (WDBC)** dataset to predict whether a tumour is malignant or benign. The key design choice: optimising for **recall over accuracy** by adjusting the classification threshold — because in a medical context, a missed cancer (false negative) is far more dangerous than a false alarm (false positive).

---

## Key design decisions

| Decision | Why |
|----------|-----|
| Recursive feature elimination (30 → 15 features) | Removes noisy features, reduces overfitting, improves generalisation |
| Threshold tuning (not just accuracy optimisation) | Prioritises recall — minimises missed malignant cases |
| Cross-validated hyperparameter search | Prevents data leakage during model selection |

---

## Results

| Metric | Value |
|--------|-------|
| Features (original) | 30 |
| Features (after RFE) | 15 |
| Optimisation target | Recall (minimise false negatives) |
| Dataset | Wisconsin Diagnostic Breast Cancer |

---

## Tech stack

- Python · scikit-learn · Pandas · NumPy
- Jupyter Notebook

---

## Files

| File | Description |
|------|-------------|
| `breast_cancer_prediction (2).ipynb` | Full pipeline — EDA, feature selection, model training, threshold tuning |

---

## How to run

```bash
pip install scikit-learn pandas numpy jupyter
jupyter notebook "breast_cancer_prediction (2).ipynb"
```

---

## Topics

`machine-learning` `classification` `healthcare` `python` `scikit-learn` `recursive-feature-elimination` `medical-ai` `breast-cancer` `recall-optimisation`


# ============================================================
# README 3 — Face-Attendance-System
# Go to that repo → click README.md → edit → paste this → commit
# ============================================================

# Face Attendance System

> Real-time biometric identity verification system — registers faces, recognises them live via webcam, and logs timestamped attendance records with unique student IDs.

**Security relevance:** Implements identity registration, biometric verification, access logging, anomaly flagging (unknown face detection), and exportable audit trails — core principles of enterprise identity management.

---

## What it does

- **Registers** new identities by capturing facial features using ORB (Oriented FAST and Rotated BRIEF) keypoint detection
- **Verifies** identities in real time from a live webcam feed using feature matching
- **Logs** attendance automatically with StudentID, Name, Date, and Time on successful match
- **Flags** unrecognised faces as "Unknown" — separating verified identities from intruders
- **Exports** full attendance records to CSV or Excel for audit purposes
- **Generates** unique hashed StudentIDs (MD5-based) for each registered person — no manual ID assignment

---

## Architecture

```
Face Registration
    └── Capture image → Extract ORB features → Store in known_faces/

Live Recognition Loop (threaded)
    └── Webcam frame → Haar Cascade face detection
        └── ORB feature extraction → Compare against registered faces
            ├── Match found → Log attendance + display name + StudentID
            └── No match → Flag as "Unknown"

Attendance Storage
    └── attendance.csv (StudentID, Name, Date, Time)
    └── students.csv (StudentID, Name, RegisteredDate)
```

---

## Tech stack

- Python · OpenCV (cv2) · Tkinter · Pandas · Pillow
- ORB feature detection · Haar Cascade classifier · MD5 hashing

---

## How to run

```bash
pip install opencv-python numpy pandas pillow
python face.py
```

**Requirements:** Webcam connected · Python 3.8+

---

## Security design notes

| Feature | Implementation |
|---------|---------------|
| Identity registration | ORB keypoint extraction + persistent storage |
| Real-time verification | Feature matching with distance threshold |
| Unknown face handling | Flagged visually, not logged as valid attendance |
| Audit trail | Full CSV log with timestamps, exportable to Excel |
| ID generation | MD5 hash of name + timestamp — collision-resistant unique IDs |

---

## Topics

`face-recognition` `identity-management` `python` `opencv` `security` `biometrics` `attendance-system` `tkinter` `orb-features` `access-logging`


# ============================================================
# README 4 — aura-202 (your UniMind / AURA aggregator project)
# Go to aura-202 repo → click README.md → edit → paste this → commit
# ============================================================

# AURA — Automated Utility and Response Agent

> A unified AI aggregator platform that routes user queries to multiple large language models simultaneously — GPT-4, Gemini, DeepSeek, and Claude — through a single interface, with side-by-side response comparison.

**Version:** 0.2 (active development — Stage 3 of 4)

---

## What this does

AURA eliminates the need to context-switch between separate AI tools. Users type one query and get responses from multiple models rendered simultaneously in a tabbed interface, making it easy to compare outputs, writing styles, and reasoning quality across models.

---

## Core features

| Feature | Description |
|---------|-------------|
| Multi-model routing | Dispatches queries to Gemini, ChatGPT, DeepSeek, Claude in parallel |
| Side-by-side comparison | Tabbed response panes — one per model |
| Image input support | Attach images to queries via file upload or Google Drive |
| Identity management | Login system with Google, Microsoft, GitHub OAuth flow |
| Sidebar model selector | Toggle which models to query per session |
| Typewriter rendering | Streamed response display with animated output |
| Cookie consent + session | Persistent login state via localStorage |

---

## Architecture

```
Frontend (ReactJS / HTML + CSS + JS)
    └── Input layer → model selector → submit

API Layer (Node.js backend)
    └── /api/gemini → Gemini 1.5 Flash
    └── [extensible to additional model endpoints]

Response normalisation
    └── Unified schema across providers
    └── Parallel Promise.all() dispatch
    └── Typewriter rendering per pane
```

---

## Tech stack

- **Frontend:** HTML5 · CSS3 · Vanilla JavaScript (v0.1–0.2) → migrating to ReactJS + Next.js (v0.3)
- **Backend:** Node.js · FastAPI (Python)
- **AI APIs:** Google Gemini 1.5 Flash · OpenAI GPT-4 · Anthropic Claude · DeepSeek
- **Auth:** Google OAuth · Microsoft OAuth · GitHub OAuth

---

## Current status

| Stage | Status | Description |
|-------|--------|-------------|
| Stage 1 | Done | Core UI + Gemini integration |
| Stage 2 | Done | Multi-model routing + tab system |
| Stage 3 | **In progress** | Backend security hardening, API key isolation, eval framework |
| Stage 4 | Planned | Full ReactJS migration + deployment |

---

## Research component

Evaluating response quality across models using **BLEU**, **ROUGE**, and human preference scoring on 500+ test prompts — methodology adapted from Google's FLAN and BIG-Bench evaluation frameworks.

---

## How to run (v0.2)

```bash
# Clone the repo
git clone https://github.com/anynomous0102/aura-202

# Add your Gemini API key in script.js
const GEMINI_API_KEY = "your_key_here";

# Open index.html in browser
# (Backend /api/gemini endpoint required for production use)
```

Get a free Gemini API key at: https://aistudio.google.com/

---

## Topics

`llm` `ai-aggregator` `multi-model` `gemini` `gpt-4` `claude` `deepseek` `javascript` `nodejs` `fastapi` `react` `nlp` `chatbot` `google-ai`
