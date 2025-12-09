
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

</p>

---

<p align="center">
  <em>This project is part of my Global Talent Visa technical portfolio, showcasing applied healthcare analytics, 
  modular Python engineering, and end-to-end digital health solution design.</em>
</p>

---

       ┌────────────────────┐
       │     Load Data      │
       │ (clinical records) │
       └─────────┬──────────┘
                 ▼
       ┌────────────────────┐
       │   Query Module     │
       │  (analytics engine)│
       └─────────┬──────────┘
                 ▼
       ┌────────────────────┐
       │  User Interface    │
       │ (menu-driven CLI)  │
       └─────────┬──────────┘
                 ▼
       ┌────────────────────┐
       │   Results Output   │
       │ (tabulate + CSV)   │
       └────────────────────┘


---

## 🩺 Digital Health Analytics Platform (Python)

This project implements a clinically oriented **Digital Health Analytics system** designed to assist clinicians in analysing vital patient indicators, identifying risk patterns, and preventing fatal heart failure outcomes. The project incorporates **data ingestion**, **intelligent query modules**, and a **fully interactive user interface**, all built in Python.

The system is implemented across three core components:

---

### 🔹 1. Data Loading & Pre-Processing
A custom-built ingestion pipeline loads clinical records from the **Heart Failure Clinical Records dataset** (UCI repository).  
Key steps include:

- CSV ingestion using `csv.DictReader`
- Error & exception handling during file loading  
- Automatic **schema mapping** into structured dictionaries  
- Type conversion for all clinical variables  
- Creation of a **unique `id` field** for each record (to support traceability & indexing)

> The implementation details are described in CHAPTER 4 of the project documentation (Implementation Report).  
:contentReference[oaicite:2]{index=2}

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

### 🔹 3. Interactive User Interface (CLI)

A structured, menu-driven CLI allows users (clinicians, analysts, students) to:

- Navigate eight health-analytics options  
- Perform quick exploratory risk analysis  
- Export analysis summaries as CSV files  
- View results in tabulated format (`tabulate` library)

The UI integrates tightly with QueryModule and is described in CHAPTER 6 program flowchart  
:contentReference[oaicite:3]{index=3}  
which illustrates:

---

## 🧠 Key Analytics Capabilities

### ✔ Age distribution analysis for fatal vs non-fatal heart failure  
### ✔ Cardiovascular risk clustering (HBP, diabetes, anaemia)  
### ✔ Analysis of patient lifestyle indicators (smoking)  
### ✔ Electrolyte and enzyme-level analysis  
### ✔ Interactive clinical decision-support queries  
### ✔ Automated CSV data persistence for reporting  

---


























## DIGITAL HEALTH ANALYTICS

![image](https://github.com/AbiodunAnalyst/DIGITAL_HEALTH_ANALYTICS/assets/110310940/16911222-4a5f-4462-8a56-a0c755d68d1e)


## INTRODUCTION
#### Digital health is transforming not only how people’s health is managed but also helping to prevent avoidable deaths. From translating health data and care into actions, it is gradually becoming an integral part of how health care providers and patients themselves manage health related problems. In addition, the availability of network enabled devices such as smartphone and wearable devices is enabling mobile medical apps and software that can provide support for clinicians to make clinical decisions using available data and artificial intelligence (AI) or machine learning (ML). 
#### The project looks at developing an interactive interface that will allow user to select from range of selection what vital health information they want to see. The project is divided into three part, the first part is where the data is loaded, the second part of the project looks at creating a query modules that contains all function and method the program want to solve  and the last which is the third part contain the user interface where all the interaction  of the query module, the data set, the menu selection, and the display code reside.
---

## PROBLEM ANALYSIS
The project is to design and analyze this dataset, and then design and implement an application that can help clinicians monitor patients’ vital signs such as blood pressure, etc. to prevent an impending fatality.
The implementation of the project will be looking at been able to:
  - Compute the average age, modal age, median age of those whose heart failure resulted in death.
  - Compute the average time taken for those whose heart failure did not result in death.
  - Compute the median age, average age, and modal age of those with high blood pressure.
  -	Compute the median age, average age, and modal age of those with diabetes.
  -	Determine whether diabetes is linked to smoking and high blood pressure.
  -	Compute the average serum sodium of those with diabetes.
  -	Determine if anaemia is linked to smoking or not.
  -	Returns anyone without high blood pressure that died of heart failure.
  -	Computes and returns the IQRs (Interquartile Range) of ejection fraction and serum creatinine.
  -	Compute and return the sample variance of creatinine phosphokinase and serum sodium.
  The outputs of any of these functions should be persisted into an external file in csv format.
  This will be achieved through proper plan of all parameter, function, method and modules that will be used.
  ---

## SOLUTION REQUIREMENT
The project solution plan is divided into three part
1.	Loading the data and this involves
  a.	Implementing a function to read the data
  b.	Implement a function to hand exception and error while load
  c.	Implement a function that read the csv file in a format required
  d.	Introduced a variable called id 
  e.	Convert the data to required data type for better out put

2.	Implement a Query Module
  a.	Implement a filter function
  b.	Implement function for every problem to be solved
3.	Implement User Interface Module
  a.	Implement a function that display what the user wants to select and see (display menu)
  b.	Implement a function that allow user to input there choice (main function)
  c.	Implement a try function
  d.	Implement a function that handle user choice
  e.	Implement a filter function that handle the death data set
  f.	Implement all the display function
---

## IMPLEMENTATION OF SOLUTION
#### The implementation started by first creating a function that will be use to read the data set for the project. The program also uses exceptional handling to handle exception and error and it is used in the project at different part for different error capturing for example when used during loading of the data set it is expected to block any exception if the file is not found. The program introduce csv.DictReader which allow the data to be read but maps the information read into a dictionary. The variable called id was introduced which makes every entry a unique entry and for proper outputting the data was also formatted to required data format for easy calculation and output.
#### The second part of the project involved the query module implementation which is the part involved with implementation of all function that defined the question the project will be solving. And also a filter function was created to filter condition to be used in the program from the data set.
#### The third part of the project which is the User Interface Module, this module contains many functions that make it easy for user to interact with the program. One of the functions is the display menu faction that display choice of different statistics that the user will like to see. Another function is the is the main function that display an interface that allow user to input that choice based on the information they want to see. The process choice function is one vital function in the project that host the choice of the user and it interact with the display function to output the required information needed by the user and the display function interact with the query module to fetch required statistics. 

#### All code are attached to the Project File
---

## PROGRAM STRUCTURE CHART

![image](https://github.com/AbiodunAnalyst/DIGITAL_HEALTH_ANALYTICS/assets/110310940/7ea98b7b-9a32-4a9e-abcc-799e58bd4a53)
---

## PROGRAM EXECUTION

You can interact with the project video [here](https://drive.google.com/file/d/1BW3Iv3hMrpxQD75kBUCzs2YCWWUqrJOq/view?usp=drive_link)
