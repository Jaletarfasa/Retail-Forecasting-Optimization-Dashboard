# CTC Decision Support Dashboard

A unified retail decision‑support dashboard integrating forecasting, promotion analytics, inventory recommendations, site selection, drift monitoring, and automated retraining logic. Built to demonstrate an end‑to‑end applied ML workflow with real operational value.

---

## 🚀 Overview

This dashboard brings together multiple analytics layers into a single interactive interface:

- **Multi‑model forecasting** (XGBoost, LightGBM, HGB, RF, ET, ElasticNet, MLP, GRU, LSTM)
- **Model comparison** with MAE, RMSE, WMAPE, MAPE, SMAPE, R², and bias
- **Store, department, region, and brand forecasts**
- **Promotion lift & margin‑lift analytics**
- **Inventory recommendations** using safety stock, lead time, pack size, and reorder caps
- **Site selection** using traffic, income, competition, rent, and projected value
- **Drift monitoring** using KS‑statistics and p‑values
- **Automated retraining triggers** with promote/no‑promote logic
- **RAG‑based agent answers** for operational questions

This project demonstrates a production‑minded architecture with clear business alignment.

---

## 📊 Key Features

### 🔹 1. Model Comparison
Evaluates champion vs challenger models using a full metric suite.  
Example from the dashboard:

- **Champion:** XGBoost  
- **MAE:** 2.8539  
- **RMSE:** 3.8191  
- **WMAPE:** 0.2117  

Includes benchmarked models for transparency and auditability.

### 🔹 2. Forecasting Layers
- **Store‑level forecasts** with margin and error diagnostics  
- **Department forecasts** (e.g., Seasonal, Outdoor Living, Home, Automotive)  
- **Region forecasts** (Ontario, Prairies, BC, Atlantic, Quebec)  
- **Brand forecasts** with unit‑level comparisons  

### 🔹 3. Promotion Analytics
Summaries include:

- **Promo lift:** 0.2955  
- **Margin lift:** 0.2029  

### 🔹 4. Inventory Recommendations
SKU‑level reorder logic using:

- Forecasted demand  
- On‑hand units  
- Lead time  
- Safety stock  
- Pack size  
- Max reorder caps  

Example:  
Store 25, SKU 15 → **Recommended reorder: 1364 units**

### 🔹 5. Site Selection
Candidate sites scored using:

- Traffic index  
- Household income index  
- Competition index  
- Rent cost  
- Space (sqft)  
- Site quality score  

### 🔹 6. Drift Monitoring & Retraining
Monitors feature drift using KS‑statistics.  
Example:

- **Drift detected:** Yes  
- **Drifted features:** 4  
- **Retraining recommended:** Yes  
- **Promotion outcome:** Candidate evaluated but not promoted  

### 🔹 7. RAG‑Based Agent Answers
Natural‑language responses to questions like:

- “What is the top forecasted department?”  
- “Which SKUs need reorder attention?”  
- “Should the model be retrained?”  

---

## 🧱 Architecture

The dashboard integrates:

- **Python / Streamlit**
- **XGBoost, LightGBM, scikit‑learn**
- **Pandas / NumPy**
- **Plotly visualizations**
- **Local TF‑IDF retrieval for RAG**
- **MLflow‑style tracking (SQLite backend)**

---

## ▶️ Running the App Locally

```bash
pip install -r requirements.txt
streamlit run dashboard_app.py
