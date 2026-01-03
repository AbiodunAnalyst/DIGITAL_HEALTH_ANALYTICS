
<h1 align="center">🩺 Digital Health Analytics Platform</h1>

<p align="center">
  <strong>Clinical Data Engineering • Python Analytics Engine • Decision Support System • Healthcare Informatics</strong>
</p>

<p align="center">
  A modular digital health analytics system designed to analyse clinical indicators, identify high-risk patient groups, 
  and support healthcare decision-making using structured Python data processing, custom query modules, and interactive reporting.
</p>

<p align="center">

  <!-- Languages -->
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />

  <!-- Health Analytics -->
  <img src="https://img.shields.io/badge/Digital%20Health-0099cc?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Clinical%20Analytics-AA3377?style=for-the-badge" />

  <!-- Tools -->
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Tabulate-4B8BBE?style=for-the-badge" />

  <!-- Status -->
  <img src="https://img.shields.io/badge/Status-Production--Ready-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" />
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white" />
</h3>
</p>

---

# 🩺 Digital Health Clinical Analytics Platform  
### AI-Driven Risk Analysis & Decision Support for Heart Failure Patients

The Digital Health Clinical Analytics Platform is an end-to-end clinical analytics system designed to support data-driven decision-making in heart failure care.
The platform enables clinicians, analysts, and researchers to explore patient risk factors, identify mortality-associated patterns, and generate interpretable insights from structured clinical data without requiring advanced coding skills.

---
My Role & Contribution
---
- Designed the system architecture
- Developed the ML engine (Model)
- Built the interactive UI
- Integrated data quality pipelines

---
🎯 Purpose & Motivation
---
Heart failure remains one of the leading causes of hospitalisation and mortality worldwide.
Despite the availability of clinical data, many healthcare teams still rely on:
- Fragmented spreadsheets
- Manual record reviews
- Static reports with limited analytical depth
- Delayed insight generation

These limitations make it difficult to:
- Detect high-risk patient profiles early
- Understand interactions between co-morbidities
- Support timely, evidence-based clinical decisions
This project was developed to bridge the gap between raw clinical data and practical clinical insight.

---
🧠 System Architecture

---

    ┌────────────────────────────┐
    │   Clinical Dataset (CSV)   │
    │  (UCI Heart Failure Data)  │
    └──────────────┬─────────────┘
                   ▼
    ┌────────────────────────────┐
    │  Data Loading & Cleaning   │
    │  (analytics.py pipeline)   │
    └──────────────┬─────────────┘
                   ▼
    ┌────────────────────────────┐
    │     Analytics Engine       │
    │ (statistics, risk logic,   │
    │  survival analysis, etc.)  │
    └──────────────┬─────────────┘
                   ▼
    ┌────────────────────────────┐
    │   Streamlit Web Interface  │
    │ (UI, charts, interaction)  │
    └──────────────┬─────────────┘
                   ▼
    ┌────────────────────────────┐
    │  Results & Predictions     │
    │ (tables, plots, CSV, ML)   │
    └────────────────────────────┘

---

**The system is implemented across three core components:**

### 🔹 1. Data Loading & Pre-Processing
A robust ingestion pipeline that converts raw clinical data into clean, structured, and traceable records.

**Key features:**
- CSV ingestion using csv.DictReader
- Defensive error and exception handling
- Automatic schema mapping into structured dictionaries
- Explicit data-type conversion for all clinical variables
- Unique patient ID generation to support traceability and indexing
This layer ensures data quality, reproducibility, and analytical integrity.

---

### 🔹 2. Analytics & Risk Engine (QueryModule)

The QueryModule class acts as the core analytical engine of the system, encapsulating reusable clinical analytics logic.

Capabilities include:

1. Descriptive & Survival Analytics
    - Age statistics (mean, median, mode) for fatal cases
    - Survival-time analysis for recovered patients
2. Risk Profiling
    - Cardiovascular risk factors:
      - High blood pressure
      - Diabetes
      - Anaemia
    - Lifestyle and condition interactions:
      - Diabetes × Smoking × High Blood Pressure
    - Serum sodium analysis for diabetic patients
    - Risk factor sampling and variance metrics:
      - Serum creatinine
      - CPK
      - Ejection fraction
3. Governance & Reproducibility
    - Automatic CSV export of analytical results
    - Supports audit, clinical validation, and research workflows

---

### 🔹 3. Interactive Web Application 

A menu-driven, clinician-friendly interface that enables users to perform advanced analytics without writing code.

**Users can:**
  - Navigate 8 structured health-analytics modules
  - Perform exploratory risk analysis
  - View results in formatted tables
  - Export outputs as CSV files
  - Visualise insights using interactive charts

**Visualisations include:**
  - Age boxplots by survival outcome
  - Survival-time distributions
  - Bar charts for risk clusters
  - Line charts for trend exploration

---

🔮 Machine Learning: Single-Patient Risk Prediction
---

The platform includes an optional AI-based risk prediction module.

Model
  - Random Forest Classifier

Input Features
  - Age
  - Anaemia
  - Diabetes
  - High blood pressure
  - Smoking
  - Ejection fraction
  - Serum creatinine
  - Serum sodium
  - Follow-up time

Outputs
  - Mortality risk prediction
  - Model performance metrics:
      - Accuracy
      - ROC-AUC
      - Confusion matrix
      - Classification report
  - Feature importance visualisation

**This module supports early risk stratification and clinical decision support.**


---

### 🚀 The Solution
To bridge this gap, I developed a **Digital Health Analytics Platform** a Web Application system that transforms raw clinical data into actionable insights.

---

### 🚀 Features

**Data ingestion**
  - Upload your own heart failure dataset (`.csv`) or use the built-in default file  
  - Automatic cleaning and typing via `analytics.py`

**Descriptive analytics**
  - Global numeric summary (mean, std, quartiles, etc.)
  - Age statistics for **fatal vs non-fatal** heart failure cases
  - Survival time analysis for recovered patients
  - Cardiometabolic risk clustering (High BP × Diabetes × Anaemia)
  - Lifestyle risk interactions (Smoking × Diabetes × High BP)
  - Serum sodium comparison for diabetic vs non-diabetic patients

**Visualisations**
    - Boxplot of age by outcome (survived vs died)
    - Line chart of survival time distribution
    - Bar charts of risk cluster distributions

**Machine learning**
    - Train a **Random Forest classifier** on the dataset
    - Adjust number of trees and max depth from the sidebar
    - See Accuracy, ROC AUC, confusion matrix, and classification report
    - Visualise feature importance
    - Use an interactive form to predict risk for a **single patient**

**Health_app** *[Health_app](https://digitalhealthanalytics-ciakssrts5fjppxcjpwmy6.streamlit.app)*

### 🩺 Clinical Impact
This platform enables healthcare teams to:
  - Detect high-risk patient profiles earlier  
  - Understand mortality-linked patterns at a glance  
  - Analyse multiple clinical and lifestyle factors simultaneously  
  - Make faster, evidence-based decisions  
  - Reduce the analytical workload for clinicians and data teams  

