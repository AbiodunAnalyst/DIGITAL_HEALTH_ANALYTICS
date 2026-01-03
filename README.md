
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
    │       ML development       │
    │ (UI, charts, interaction)  │
    └──────────────┬─────────────┘
                   ▼
    ┌────────────────────────────┐
    │       Web Interface        │
    │ (UI, charts, interaction)  │
    └──────────────┬─────────────┘
                   ▼
    ┌────────────────────────────┐
    │  Results & Predictions     │
    │ (tables, plots, CSV, ML)   │
    └────────────────────────────┘

---

**The system is implemented across four core components:**

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

### 🔹 3. Machine Learning: Single-Patient Risk Prediction
---
**Development Phase**
---
1. **Data Quality steps**:
  I implemented data quality checks which includes:
    - Missing value handling strategy
    - Outlier detection
    - Feature validation
    - Data leakage prevention
---
Considering the clinical setting and the necessity for comprehensible yet effective risk predictions, I assessed various imbalanced data techniques and machine learning models to determine the most suitable method for forecasting patient risk outcomes. 

2. **Handing Imbalanced data**:
  I compare different imbalanced method such as:
    - BorderlineSMOTE
    - TomekLinks
    - SMOTE
    - RandomOverSampler

3. **Machine learning model**:
  I compare different Machine learning model such as:
    - Random forest model
    - Logistic regression model
    - Support vector model

4. **Optimization Method**
  - GridSearchCV
---

5. **Model Validation & Evaluation**: I implemented Model Validation & Evaluation which includes:
  - Train/test split 
  - Metric selection justification
  - ROC-AUC 
  - Confusion matrix

The dataset was split into training and test sets to evaluate generalisation. Model performance was assessed using precision, recall, F1-score, accuracy, and ROC-AUC to reflect the clinical risk prediction context. ROC-AUC was prioritised due to class imbalance and the need for threshold-independent discrimination. Confusion matrix analysis was used to examine false positives and false negatives. Comparison of training and test ROC-AUC scores indicated strong generalisation without significant overfitting.

---
**Model performance comparism**

Random Forest model + Tomeklink

<img width="209" height="252" alt="image" src="https://github.com/user-attachments/assets/292b38c1-6543-4ed2-bf7c-db918dc89a35" />

fig-1

Logistic regression + SMOTE

<img width="212" height="240" alt="image" src="https://github.com/user-attachments/assets/cf473646-5212-45ca-8c0c-c4e8d8ae1a30" />

fig-2

Support vector model +  Tomeklink

<img width="212" height="238" alt="image" src="https://github.com/user-attachments/assets/ad86bb10-01b0-4f8f-b872-de63db267d28" />

fig-3

Random Forest model + Tomeklink + baseline data

<img width="200" height="245" alt="image" src="https://github.com/user-attachments/assets/fb2ab411-9f2f-489e-8279-1ecc55d474d4" />

fig-4

Logistic regression + Borderline SMOTE

<img width="212" height="239" alt="image" src="https://github.com/user-attachments/assets/edc30935-f122-41c6-8293-bbec4c7d0e7d" />

fig-5

Random Forest model + Random oversampler + Gridsearch

<img width="211" height="245" alt="image" src="https://github.com/user-attachments/assets/41edf623-c94a-47ea-acf0-52b2db46294f" />

fig-6

---
### 🔹 4. Web Application 
To bridge this gap, I developed a **Digital Health Analytics Platform**, a Web Application system that transforms raw clinical data into actionable insights.

---

### Development Phase
###  **Web Application Development**
    The web application was developed using Python within Visual Studio Code, enabling rapid iteration, debugging, and version control during the development process.
  
###  **Core Libraries and Frameworks**
    - Streamlit - for building and deploying an interactive web-based analytics interface
    - Pandas & NumPy - for data manipulation and numerical computation
    - Matplotlib - for data visualisation
    - Scikit-learn - for machine learning model development and evaluation
###  **Deployment Platform**
    - The application was deployed using Streamlit, allowing the analytics platform and machine learning model to be accessed through a lightweight, browser-based interface without requiring complex infrastructure.
    - Streamlit was selected for deployment due to its suitability for rapid prototyping of data-driven applications and its ability to make analytical insights accessible to non-technical users.

### 🚀 Solution Features

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

### **Visualisations**
    - Boxplot of age by outcome (survived vs died)
    - Line chart of survival time distribution
    - Bar charts of risk cluster distributions

### **Machine learning**
    - Predict risk for a single patient

**Health_app** *[Health_app](https://digitalhealthanalytics-ciakssrts5fjppxcjpwmy6.streamlit.app)*

### 🩺   Solution Clinical Impact
This platform enables healthcare teams to:
  - Detect high-risk patient profiles earlier  
  - Understand mortality-linked patterns at a glance  
  - Analyse multiple clinical and lifestyle factors simultaneously  
  - Make faster, evidence-based decisions  
  - Reduce the analytical workload for clinicians and data teams  

