import os
import pandas as pd
import streamlit as st

st.set_page_config(page_title="CTC Decision Support Dashboard", layout="wide")
st.title("CTC Decision Support Dashboard")


def load_csv(filename: str) -> pd.DataFrame:
    """
    Load a CSV file safely and stop the app with a clear message if missing.
    """
    if not os.path.exists(filename):
        st.error(f"Missing file: {filename}")
        st.stop()
    return pd.read_csv(filename)


# -------------------------------------------------------------------
# Data loading
# -------------------------------------------------------------------
exec_df = load_csv("dashboard_executive_summary.csv")
model_df = load_csv("dashboard_model_comparison.csv")
store_df = load_csv("dashboard_store_forecast.csv")
dept_df = load_csv("dashboard_department_forecast.csv")
region_df = load_csv("dashboard_region_forecast.csv")
brand_df = load_csv("dashboard_brand_forecast.csv")
drift_df = load_csv("drift_monitor.csv")
retrain_df = load_csv("retraining_status.csv")
retrain_audit_df = load_csv("retraining_audit.csv")
reorder_df = load_csv("inventory_recommendations.csv")
site_df = load_csv("optimized_site_selection.csv")
agent_df = load_csv("agent_answers.csv")
watch_df = load_csv("store_watchlist.csv")
maturity_df = load_csv("dashboard_pipeline_maturity.csv")


# -------------------------------------------------------------------
# Executive Summary
# -------------------------------------------------------------------
st.subheader("Executive Summary")
st.dataframe(exec_df, use_container_width=True)

# -------------------------------------------------------------------
# Model Comparison
# -------------------------------------------------------------------
st.subheader("Model Comparison")
if "mae" in model_df.columns:
    st.dataframe(model_df.sort_values("mae", ascending=True), use_container_width=True)
else:
    st.dataframe(model_df, use_container_width=True)

# -------------------------------------------------------------------
# Store and Department Forecasts
# -------------------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Store Forecast")
    if "forecast_units" in store_df.columns:
        st.dataframe(
            store_df.sort_values("forecast_units", ascending=False),
            use_container_width=True
        )
    else:
        st.dataframe(store_df, use_container_width=True)

with col2:
    st.subheader("Department Forecast")
    if "forecast_units" in dept_df.columns:
        st.dataframe(
            dept_df.sort_values("forecast_units", ascending=False),
            use_container_width=True
        )
    else:
        st.dataframe(dept_df, use_container_width=True)

# -------------------------------------------------------------------
# Region Forecast
# -------------------------------------------------------------------
st.subheader("Region Forecast")
if "forecast_units" in region_df.columns:
    st.dataframe(
        region_df.sort_values("forecast_units", ascending=False),
        use_container_width=True
    )
else:
    st.dataframe(region_df, use_container_width=True)

# -------------------------------------------------------------------
# Brand Forecast
# -------------------------------------------------------------------
st.subheader("Brand Forecast")
if "forecast_units" in brand_df.columns:
    st.dataframe(
        brand_df.sort_values("forecast_units", ascending=False),
        use_container_width=True
    )
else:
    st.dataframe(brand_df, use_container_width=True)

# -------------------------------------------------------------------
# Drift Monitor
# -------------------------------------------------------------------
st.subheader("Drift Monitor")
st.dataframe(drift_df, use_container_width=True)

# -------------------------------------------------------------------
# Retraining Status
# -------------------------------------------------------------------
st.subheader("Retraining Status")
st.dataframe(retrain_df, use_container_width=True)

# -------------------------------------------------------------------
# Retraining Audit
# -------------------------------------------------------------------
st.subheader("Retraining Audit")
st.dataframe(retrain_audit_df, use_container_width=True)

# -------------------------------------------------------------------
# Inventory Recommendations
# -------------------------------------------------------------------
st.subheader("Inventory Recommendations")
sort_cols = [col for col in ["urgent_reorder_flag", "recommended_reorder_qty"] if col in reorder_df.columns]

if len(sort_cols) == 2:
    st.dataframe(
        reorder_df.sort_values(
            ["urgent_reorder_flag", "recommended_reorder_qty"],
            ascending=[False, False]
        ),
        use_container_width=True
    )
else:
    st.dataframe(reorder_df, use_container_width=True)

# -------------------------------------------------------------------
# Optimized Site Selection
# -------------------------------------------------------------------
st.subheader("Optimized Site Selection")
if "projected_value_index" in site_df.columns:
    st.dataframe(
        site_df.sort_values("projected_value_index", ascending=False),
        use_container_width=True
    )
else:
    st.dataframe(site_df, use_container_width=True)

# -------------------------------------------------------------------
# Store Watchlist
# -------------------------------------------------------------------
st.subheader("Store Watchlist")
st.dataframe(watch_df, use_container_width=True)

# -------------------------------------------------------------------
# Agent Answers
# -------------------------------------------------------------------
st.subheader("Agent Answers")
st.dataframe(agent_df, use_container_width=True)

# -------------------------------------------------------------------
# Implementation Maturity
# -------------------------------------------------------------------
st.subheader("Implementation Maturity")
st.dataframe(maturity_df, use_container_width=True)