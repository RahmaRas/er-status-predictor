import streamlit as st
import joblib
import json
import numpy as np
import pandas as pd

model = joblib.load('er_model.pkl')
scaler = joblib.load('er_scaler.pkl')
selector = joblib.load('er_selector.pkl')
with open('selected_genes.json') as f:
    all_genes = json.load(f)

st.title("Breast Cancer ER Status Predictor")
st.write("Upload a gene expression CSV file to predict ER status.")

uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file, index_col=0)
    df = df[~df.index.astype(str).str.contains('Gene|Entrez', case=False)]
    st.write("Uploaded data shape:", df.shape)
    shared = [g for g in all_genes if g in df.columns]
    st.write("Shared genes found:", len(shared))
    X = df[shared].reindex(columns=all_genes, fill_value=0)
    X_scaled = scaler.transform(X)
    X_sel = selector.transform(X_scaled)
    probs = model.predict_proba(X_sel)[:, 1]
    preds = (probs >= 0.43).astype(int)
    results = pd.DataFrame({
        'Patient': df.index,
        'Prediction': ['ER Positive' if p == 1 else 'ER Negative' for p in preds],
        'Confidence': [f"{p:.1%}" for p in probs]
    })
    st.subheader("Results")
    st.dataframe(results)
