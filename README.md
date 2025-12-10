
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

The Digital Health Analytics Platform is an end-to-end clinical analytics system designed to help clinicians, data analysts, and researchers analyse heart-failure patient data, uncover hidden risk patterns, and support early clinical decision-making.

It combines:

- Automated data ingestion & cleaning
- A reusable analytics engine (statistics + risk profiling)
- An interactive Streamlit web interface
- Optional ML-based single-patient risk prediction
- Built using Python, Streamlit, Pandas, and Scikit-Learn, the platform transforms raw clinical data into interpretable visual insights that support proactive healthcare.

---

The system is implemented across three core components:

### 🔹 1. Data Loading & Pre-Processing
A custom-built ingestion pipeline loads clinical records from the **Heart Failure Clinical Records dataset**.  
Key steps include:

- CSV ingestion using `csv.DictReader`
- Error & exception handling during file loading  
- Automatic **schema mapping** into structured dictionaries  
- Type conversion for all clinical variables  
- Creation of a **unique `id` field** for each record (to support traceability & indexing)

---

### 🔹 2. Query Module (Analytics & Risk Functions)

The **QueryModule** class encapsulates all analytical functions the system provides.  
It supports:

- **Age statistics** (average, median, mode) for patients whose heart failure resulted in death  
- **Survival-time analysis** for patients who recovered  
- **Cardiovascular risk profiling** for:
  - high blood pressure  
  - diabetes  
  - anaemia  
- **Risk interaction analysis**:
  - diabetes × smoking × high blood pressure  
- **Serum sodium analysis** for diabetic patients  
- **Risk factor sampling & variance metrics** (serum creatinine, CPK, etc.)
- **Automatic CSV export** of all results for clinical audit or reporting

This module acts as the system’s *analytics engine*.

---

### 🔹 3. Interactive Streamlt Application 

A structured, menu-driven application that allows users (clinicians, analysts, students) to:

- Navigate eight health-analytics options  
- Perform quick exploratory risk analysis  
- Export analysis summaries as CSV files  
- View results in tabulated format (`tabulate` library)
- Visualisations:
  - Age boxplot by outcome
  - Survival time distribution
  - Line charts
  - Bar charts for grouped risk clusters
- ML prediction

---

🔮 Single Patient Risk Prediction

Uses a pre-trained Random Forest classifier to estimate mortality risk for a new patient based on:
- Age
- Anaemia
- Diabetes
- High BP
- Smoking
- Ejection fraction
- Serum creatinine
- Serum sodium
- Follow-up time

---



##  System Architecture diagram

                   ┌────────────────────────┐
                   │   Clinical Dataset      │
                   │ (CSV – UCI Repository)  │
                   └───────────┬────────────┘
                               ▼
                 ┌────────────────────────────┐
                 │  Data Loading & Cleaning   │
                 │  (analytics.py pipeline)   │
                 └───────────┬───────────────┘
                               ▼
                 ┌────────────────────────────┐
                 │     Analytics Engine       │
                 │ (risk profiling, stats,    │
                 │  survival analysis, etc.)  │
                 └───────────┬───────────────┘
                               ▼
              ┌───────────────────────────────────┐
              │        Streamlit Application       │
              │ (UI, charts, menu-driven analysis) │
              └───────────┬───────────────────────┘
                          ▼
              ┌───────────────────────────────────┐
              │        Results & Predictions       │
              │ (tables, plots, CSV export, ML)    │
              └───────────────────────────────────┘



---

## 🩺 Problem → Solution Narrative

### 🔍 The Problem
Heart failure remains one of the leading causes of hospitalisation and mortality worldwide.  
Clinicians frequently rely on fragmented spreadsheets, manual review, or delayed reporting to understand patient risks and identify deterioration patterns.

Key challenges include:

- Disconnected and inconsistently formatted clinical datasets  
- Limited ability to quickly explore mortality-associated risk factors  
- Difficulty analysing interactions between conditions (e.g., diabetes × hypertension × smoking)  
- No simple tool for clinicians to run data-driven queries without coding  
- Lack of automated exports for audits, research, or quality improvement  

This leads to:
- Missed high-risk patterns
- Slow decision-making
- No easy understanding of interactions between conditions (e.g., diabetes × hypertension × smoking)
- No accessible analytics tools for clinicians who cannot code

---

### 🚀 The Solution
To bridge this gap, I developed a **Digital Health Analytics Platform** a Streamlit Web Application system that transforms raw clinical data into actionable insights.

---

### 🚀 Features

- **Data ingestion**
  - Upload your own heart failure dataset (`.csv`) or use the built-in default file  
  - Automatic cleaning and typing via `analytics.py`

- **Descriptive analytics**
  - Global numeric summary (mean, std, quartiles, etc.)
  - Age statistics for **fatal vs non-fatal** heart failure cases
  - Survival time analysis for recovered patients
  - Cardiometabolic risk clustering (High BP × Diabetes × Anaemia)
  - Lifestyle risk interactions (Smoking × Diabetes × High BP)
  - Serum sodium comparison for diabetic vs non-diabetic patients

- **Visualisations**
  - Boxplot of age by outcome (survived vs died)
  - Line chart of survival time distribution
  - Bar charts of risk cluster distributions

- **Machine learning**
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

