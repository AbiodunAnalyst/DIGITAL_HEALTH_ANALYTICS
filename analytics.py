# analytics.py

"""
Digital Health Analytics – Core Analytics Module

This module contains reusable functions for:
- Loading and cleaning clinical data
- Computing key statistics and risk profiles
- Returning results as pandas DataFrames/Series for use in Streamlit
"""

from typing import Tuple
import pandas as pd
import numpy as np


# -----------------------------------------
# Default dataset path (same folder)
# -----------------------------------------

DEFAULT_DATA_PATH = "heart_failure_clinical_records_dataset-pcp.csv"


# ------------------------
# Data loading & cleaning
# ------------------------

def load_clinical_data(path: str = DEFAULT_DATA_PATH) -> pd.DataFrame:
    """
    Load the heart failure clinical dataset from a CSV file.

    Expected columns (your dataset style):
    - id, age, anaemia, creatinine_phosphokinase, diabetes,
      ejection_fraction, high_blood_pressure, platelets,
      serum_creatinine, serum_sodium, gender, smoking, time, DEATH_EVENT
    """
    df = pd.read_csv(path)

    # Standardise column names: lowercase, strip spaces
    df.columns = [c.strip().lower() for c in df.columns]

    # Optional: rename some known columns for consistency
    rename_map = {
        "death_event": "death_event",
        "high_blood_pressure": "high_blood_pressure",
        "creatinine_phosphokinase": "cpk",
        "serum_creatinine": "serum_creatinine",
        "serum_sodium": "serum_sodium",
    }
    df = df.rename(columns=rename_map)

    # Ensure numeric types where expected
    numeric_cols = [
        "id",
        "age", "anaemia", "diabetes", "high_blood_pressure", "smoking",
        "ejection_fraction", "platelets", "serum_creatinine", "serum_sodium",
        "time", "death_event"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Drop completely empty rows if any
    df = df.dropna(how="all")

    return df


# ------------------------
# Helper: split by outcome
# ------------------------

def split_by_outcome(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Split dataset into:
    - fatal: death_event == 1
    - non_fatal: death_event == 0
    """
    if "death_event" not in df.columns:
        raise ValueError("Expected column 'death_event' not found in dataframe.")

    fatal = df[df["death_event"] == 1]
    non_fatal = df[df["death_event"] == 0]
    return fatal, non_fatal


# ------------------------
# Analytics functions
# ------------------------

def age_stats_fatal_vs_nonfatal(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return descriptive statistics of age for fatal vs non-fatal cases.
    """
    fatal, non_fatal = split_by_outcome(df)

    stats = {
        "Group": ["Fatal (DEATH_EVENT=1)", "Non-fatal (DEATH_EVENT=0)"],
        "Count": [fatal["age"].count(), non_fatal["age"].count()],
        "Mean Age": [fatal["age"].mean(), non_fatal["age"].mean()],
        "Median Age": [fatal["age"].median(), non_fatal["age"].median()],
        "Min Age": [fatal["age"].min(), non_fatal["age"].min()],
        "Max Age": [fatal["age"].max(), non_fatal["age"].max()],
    }
    return pd.DataFrame(stats)


def survival_time_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return survival time statistics for recovered patients (DEATH_EVENT=0).
    """
    if "time" not in df.columns:
        raise ValueError("Expected column 'time' not found in dataframe.")

    _, non_fatal = split_by_outcome(df)
    series = non_fatal["time"]

    desc = series.describe(percentiles=[0.25, 0.5, 0.75]).to_frame(
        name="Survival days (recovered)"
    )
    return desc


def cardiometabolic_risk_profile(df: pd.DataFrame) -> pd.DataFrame:
    """
    Group patients by High Blood Pressure, Diabetes, and Anaemia.
    Shows count of patients in each risk cluster.
    """
    required_cols = ["high_blood_pressure", "diabetes", "anaemia"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns for cardiometabolic risk: {missing}")

    grouped = (
        df.groupby(["high_blood_pressure", "diabetes", "anaemia"])
        .size()
        .reset_index(name="patient_count")
        .sort_values("patient_count", ascending=False)
    )

    # Convert 0/1 to Yes/No labels
    label_map = {0: "No", 1: "Yes"}
    for col in ["high_blood_pressure", "diabetes", "anaemia"]:
        grouped[col] = grouped[col].map(label_map)

    return grouped


def lifestyle_risk_interaction(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analyse interaction between smoking, diabetes, and high blood pressure.
    Returns grouped patient counts.
    """
    required_cols = ["smoking", "diabetes", "high_blood_pressure"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns for lifestyle risk analysis: {missing}")

    grouped = (
        df.groupby(["smoking", "diabetes", "high_blood_pressure"])
        .size()
        .reset_index(name="patient_count")
        .sort_values("patient_count", ascending=False)
    )

    # Map 0/1 to Yes/No
    label_map = {0: "No", 1: "Yes"}
    for col in ["smoking", "diabetes", "high_blood_pressure"]:
        grouped[col] = grouped[col].map(label_map)

    return grouped


def serum_sodium_stats_for_diabetics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute serum sodium statistics for diabetic vs non-diabetic patients.
    """
    if "serum_sodium" not in df.columns or "diabetes" not in df.columns:
        raise ValueError("Expected columns 'serum_sodium' and 'diabetes' not found.")

    diabetic = df[df["diabetes"] == 1]["serum_sodium"]
    non_diabetic = df[df["diabetes"] == 0]["serum_sodium"]

    stats = {
        "Group": ["Diabetic", "Non-diabetic"],
        "Count": [diabetic.count(), non_diabetic.count()],
        "Mean Sodium": [diabetic.mean(), non_diabetic.mean()],
        "Std Sodium": [diabetic.std(), non_diabetic.std()],
        "Min Sodium": [diabetic.min(), non_diabetic.min()],
        "Max Sodium": [diabetic.max(), non_diabetic.max()],
    }
    return pd.DataFrame(stats)


def global_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return descriptive statistics for all numeric columns.
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    return df[numeric_cols].describe().T
