# Health_app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    roc_auc_score,
    classification_report,
    confusion_matrix,
)

from analytics import (
    load_clinical_data,
    age_stats_fatal_vs_nonfatal,
    survival_time_stats,
    cardiometabolic_risk_profile,
    lifestyle_risk_interaction,
    serum_sodium_stats_for_diabetics,
    global_summary,
)


# --------------------------
# Streamlit page config
# --------------------------
st.set_page_config(
    page_title="Digital Health Analytics Platform",
    page_icon="🩺",
    layout="wide",
)

st.title("🩺 Digital Health Analytics Platform")
st.caption("Heart failure clinical records – exploratory risk analysis, visualisation, and risk prediction")

st.markdown(
    """
This application allows clinicians, analysts, and students to explore heart failure clinical data, 
understand risk patterns, and train a simple machine learning model to predict mortality risk.
"""
)

st.markdown("---")

# --------------------------
# Data loading section
# --------------------------
st.sidebar.header("1️⃣ Load Clinical Dataset")

uploaded_file = st.sidebar.file_uploader("Upload heart failure CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.sidebar.success("Custom dataset loaded.")
else:
    try:
        df = load_clinical_data()  # uses DEFAULT_DATA_PATH from analytics.py
        st.sidebar.info("Using default dataset: `heart_failure_clinical_records_dataset-pcp.csv`")
    except FileNotFoundError:
        st.error("No dataset found. Please upload a CSV file using the sidebar.")
        st.stop()

st.subheader("📋 Data Preview")
st.dataframe(df.head(), use_container_width=True)

with st.expander("Show dataset info"):
    st.write("Shape:", df.shape)
    st.write("Columns:", list(df.columns))

st.markdown("---")

# --------------------------
# Sidebar: Analysis selection
# --------------------------
st.sidebar.header("2️⃣ Choose Analysis or Model")

analysis_options = [
    "Global numeric summary",
    "Age statistics – fatal vs non-fatal cases",
    "Survival time – recovered patients",
    "Cardiometabolic risk profile (HBP × Diabetes × Anaemia)",
    "Lifestyle risk interaction (Smoking × Diabetes × HBP)",
    "Serum sodium – diabetic vs non-diabetic patients",
    "Visualisations – Age & Survival",
    "Machine learning – Random Forest risk prediction",
]

analysis_choice = st.sidebar.selectbox("Select an option", analysis_options)

result_df = None
title = ""
description = ""

# --------------------------
# Analysis logic
# --------------------------
try:
    if analysis_choice == "Global numeric summary":
        title = "📊 Global Numeric Summary"
        description = (
            "High-level descriptive statistics for all numeric variables "
            "in the dataset (mean, std, quartiles, min, max)."
        )
        result_df = global_summary(df)

    elif analysis_choice == "Age statistics – fatal vs non-fatal cases":
        title = "👵 Age Statistics – Fatal vs Non-fatal Heart Failure Cases"
        description = (
            "Comparison of age distribution between patients who died "
            "and those who survived within the observation window."
        )
        result_df = age_stats_fatal_vs_nonfatal(df)

    elif analysis_choice == "Survival time – recovered patients":
        title = "⏱ Survival Time – Recovered Patients (DEATH_EVENT=0)"
        description = (
            "Survival time summary (in days) for patients who did not die during the study period."
        )
        result_df = survival_time_stats(df)

    elif analysis_choice == "Cardiometabolic risk profile (HBP × Diabetes × Anaemia)":
        title = "❤️ Cardiometabolic Risk Profile"
        description = (
            "Counts of patients across combinations of high blood pressure, diabetes, "
            "and anaemia. Useful for understanding multi-morbidity clusters."
        )
        result_df = cardiometabolic_risk_profile(df)

    elif analysis_choice == "Lifestyle risk interaction (Smoking × Diabetes × HBP)":
        title = "🚬 Lifestyle & Clinical Risk Interaction"
        description = (
            "Distribution of patients based on smoking status, diabetes, and high blood pressure. "
            "Helps explore lifestyle × clinical interactions."
        )
        result_df = lifestyle_risk_interaction(df)

    elif analysis_choice == "Serum sodium – diabetic vs non-diabetic patients":
        title = "🧪 Serum Sodium – Diabetic vs Non-diabetic Patients"
        description = (
            "Comparison of serum sodium levels between diabetic and non-diabetic patients."
        )
        result_df = serum_sodium_stats_for_diabetics(df)

except Exception as e:
    st.error(f"An error occurred while running the analysis: {e}")
    st.stop()

# --------------------------
# Display tabular results
# --------------------------
if analysis_choice not in [
    "Visualisations – Age & Survival",
    "Machine learning – Random Forest risk prediction",
]:
    if result_df is not None:
        st.subheader(title)
        st.write(description)
        st.dataframe(result_df, use_container_width=True)

        # Charts for grouped counts
         # Charts for grouped counts
        if analysis_choice in [
            "Cardiometabolic risk profile (HBP × Diabetes × Anaemia)",
            "Lifestyle risk interaction (Smoking × Diabetes × HBP)",
        ] and "patient_count" in result_df.columns:
            st.markdown("#### 📈 Distribution Chart")

            # All columns except the count column
            index_cols = [c for c in result_df.columns if c != "patient_count"]

            # Create a combined label for each group, e.g. "Yes | No | Yes"
            plot_df = result_df.copy()
            plot_df["group"] = plot_df[index_cols].astype(str).agg(" | ".join, axis=1)

            # Use the group label as index
            plot_df = plot_df.set_index("group")

            # Plot patient_count
            st.bar_chart(plot_df["patient_count"])

        # Download results as CSV
        csv = result_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download results as CSV",
            data=csv,
            file_name="digital_health_analysis_result.csv",
            mime="text/csv",
        )

# --------------------------
# Visualisations
# --------------------------
if analysis_choice == "Visualisations – Age & Survival":
    st.subheader("📊 Visualisations – Age & Survival")

    col1, col2 = st.columns(2)

    # Boxplot: Age by outcome
    with col1:
        st.markdown("#### Age Distribution by Outcome (Boxplot)")
        if "age" in df.columns and "death_event" in df.columns:
            fig, ax = plt.subplots()
            df.boxplot(column="age", by="death_event", ax=ax)
            ax.set_xlabel("DEATH_EVENT (0 = survived, 1 = died)")
            ax.set_ylabel("Age")
            ax.set_title("Age Distribution by Outcome")
            plt.suptitle("")
            st.pyplot(fig)
        else:
            st.warning("Columns 'age' and 'death_event' are required for this plot.")

    # Line chart: survival time distribution
    with col2:
        st.markdown("#### Survival Time Distribution (Line Chart)")
        if "time" in df.columns:
            time_counts = df["time"].value_counts().sort_index()
            st.line_chart(time_counts)
        else:
            st.warning("Column 'time' is required for this plot.")

# --------------------------
# Machine learning – Random Forest
# --------------------------
if analysis_choice == "Machine learning – Random Forest risk prediction":
    st.subheader("🤖 Machine Learning – Random Forest Risk Prediction")

    # Define features and target
    required_cols = [
        "age",
        "anaemia",
        "diabetes",
        "high_blood_pressure",
        "smoking",
        "ejection_fraction",
        "platelets",
        "serum_creatinine",
        "serum_sodium",
        "time",
        "death_event",
    ]

    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        st.error(f"Missing required columns for modelling: {missing}")
        st.stop()

    X = df[
        [
            "age",
            "anaemia",
            "diabetes",
            "high_blood_pressure",
            "smoking",
            "ejection_fraction",
            "platelets",
            "serum_creatinine",
            "serum_sodium",
            "time",
        ]
    ]
    y = df["death_event"]

    # Handle any remaining missing values
    X = X.fillna(X.median(numeric_only=True))

    test_size = st.sidebar.slider("Test size (fraction)", 0.1, 0.5, 0.3, 0.05)
    random_state = 42

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )

 # --- Silent model training (no metrics shown) ---
    n_estimators = 150
    max_depth = 8
    random_state = 42

    rf = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=random_state,
        class_weight="balanced",
    )
    rf.fit(X_train, y_train)

    # --------------------------
    # Interactive single-patient prediction
    # --------------------------
    st.markdown("---")
    st.markdown("### 🔮 Single Patient Risk Prediction")

    with st.form("prediction_form"):
        col_a, col_b, col_c = st.columns(3)

        with col_a:
            age = st.number_input("Age", min_value=1, max_value=120, value=60)
            anaemia = st.selectbox("Anaemia (0 = No, 1 = Yes)", [0, 1], index=0)
            diabetes = st.selectbox("Diabetes (0 = No, 1 = Yes)", [0, 1], index=0)
            high_bp = st.selectbox("High Blood Pressure (0 = No, 1 = Yes)", [0, 1], index=0)

        with col_b:
            smoking = st.selectbox("Smoking (0 = No, 1 = Yes)", [0, 1], index=0)
            ejection_fraction = st.number_input("Ejection Fraction (%)", min_value=5, max_value=80, value=35)
            platelets = st.number_input("Platelets (kiloplatelets/mL)", min_value=10000, max_value=1000000, value=250000)

        with col_c:
            serum_creatinine = st.number_input("Serum Creatinine (mg/dL)", min_value=0.1, max_value=15.0, value=1.0)
            serum_sodium = st.number_input("Serum Sodium (mEq/L)", min_value=100, max_value=200, value=138)
            time_val = st.number_input("Follow-up Time (days)", min_value=0, max_value=300, value=120)

        submitted = st.form_submit_button("Predict Risk")

    if submitted:
        input_df = pd.DataFrame(
            [
                {
                    "age": age,
                    "anaemia": anaemia,
                    "diabetes": diabetes,
                    "high_blood_pressure": high_bp,
                    "smoking": smoking,
                    "ejection_fraction": ejection_fraction,
                    "platelets": platelets,
                    "serum_creatinine": serum_creatinine,
                    "serum_sodium": serum_sodium,
                    "time": time_val,
                }
            ]
        )

        # Predict probability of death
        proba = rf.predict_proba(input_df)[0, 1]
        pred_class = rf.predict(input_df)[0]

        st.markdown("#### Prediction Result")
        st.write(f"**Predicted risk of death event:** `{proba:.3f}`")
        if pred_class == 1:
            st.error("⚠ The model predicts a **high risk** of death .")
        else:
            st.success("✅ The model predicts **low risk** of death .")
