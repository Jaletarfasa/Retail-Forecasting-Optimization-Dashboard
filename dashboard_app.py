
import sqlite3
import pandas as pd
import streamlit as st

DB = r"C:\Users\S.Tarfasa\Desktop\Data Scientist_2026\ctc_enterprise.db"
conn = sqlite3.connect(DB)

st.set_page_config(page_title="CTC Decision Support Dashboard", layout="wide")
st.title("CTC Decision Support Dashboard")

exec_df = pd.read_sql("SELECT * FROM dashboard_executive_summary", conn)
model_df = pd.read_sql("SELECT * FROM dashboard_model_comparison", conn)
store_df = pd.read_sql("SELECT * FROM dashboard_store_forecast", conn)
dept_df = pd.read_sql("SELECT * FROM dashboard_department_forecast", conn)
region_df = pd.read_sql("SELECT * FROM dashboard_region_forecast", conn)
brand_df = pd.read_sql("SELECT * FROM dashboard_brand_forecast", conn)
drift_df = pd.read_sql("SELECT * FROM drift_monitor", conn)
retrain_df = pd.read_sql("SELECT * FROM retraining_status", conn)
retrain_audit_df = pd.read_sql("SELECT * FROM retraining_audit", conn)
reorder_df = pd.read_sql("SELECT * FROM inventory_recommendations", conn)
site_df = pd.read_sql("SELECT * FROM optimized_site_selection", conn)
agent_df = pd.read_sql("SELECT * FROM agent_answers", conn)
watch_df = pd.read_sql("SELECT * FROM store_watchlist", conn)
maturity_df = pd.read_sql("SELECT * FROM dashboard_pipeline_maturity", conn)

st.subheader("Executive Summary")
st.dataframe(exec_df, use_container_width=True)

st.subheader("Model Comparison")
st.dataframe(model_df.sort_values("mae", ascending=True), use_container_width=True)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Store Forecast")
    st.dataframe(store_df.sort_values("forecast_units", ascending=False), use_container_width=True)
with col2:
    st.subheader("Department Forecast")
    st.dataframe(dept_df.sort_values("forecast_units", ascending=False), use_container_width=True)

st.subheader("Region Forecast")
st.dataframe(region_df.sort_values("forecast_units", ascending=False), use_container_width=True)

st.subheader("Brand Forecast")
st.dataframe(brand_df.sort_values("forecast_units", ascending=False), use_container_width=True)

st.subheader("Drift Monitor")
st.dataframe(drift_df, use_container_width=True)

st.subheader("Retraining Status")
st.dataframe(retrain_df, use_container_width=True)

st.subheader("Retraining Audit")
st.dataframe(retrain_audit_df, use_container_width=True)

st.subheader("Inventory Recommendations")
st.dataframe(
    reorder_df.sort_values(["urgent_reorder_flag", "recommended_reorder_qty"], ascending=[False, False]),
    use_container_width=True
)

st.subheader("Optimized Site Selection")
st.dataframe(site_df.sort_values("projected_value_index", ascending=False), use_container_width=True)

st.subheader("Store Watchlist")
st.dataframe(watch_df, use_container_width=True)

st.subheader("Agent Answers")
st.dataframe(agent_df, use_container_width=True)

st.subheader("Implementation Maturity")
st.dataframe(maturity_df, use_container_width=True)
