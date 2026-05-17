# ER Status Predictor — Trustworthy Genomic AI

Predicting breast cancer estrogen receptor (ER) status from RNA-seq gene expression data, with a focus on model stability, fairness, and explainability — not just accuracy.

**Live app:** https://rasrahma06-rahmaras-er-predictor.hf.space

## What this project does

Most genomic ML projects stop at accuracy. This one goes further — evaluating whether a model is actually trustworthy enough for clinical use by measuring stability, bias, and biological validity alongside predictive performance.

- Predicts ER+ vs ER− status from 20,530-gene RNA-seq profiles
- Achieves ROC-AUC 0.95 on TCGA BRCA (780 patients)
- Validates externally on METABRIC (1,937 independent patients)
- Explains predictions using SHAP — top genes match known biology (ESR1, GATA3, AGR3)
- Corrects class imbalance bias using SMOTE, reducing accuracy gap from 8.1% to 3.6%
- Deployed as an interactive clinical web app with downloadable reports

## Results

| Metric | Value |
|---|---|
| Internal ROC-AUC (TCGA) | 0.950 |
| Bootstrap 95% CI | [0.896, 0.994] |
| External ROC-AUC (METABRIC) | 0.696 |
| Feature stability (Jaccard) | 0.529 |
| Bias gap after SMOTE | 3.6% |
| HER2 prediction AUC | 0.929 |

## Tech stack

Python · scikit-learn · SHAP · SMOTE · BioGPT · Streamlit · Docker · Hugging Face Spaces

## How to run locally

```bash
git clone https://github.com/RahmaRas/er-status-predictor
cd er-status-predictor
pip install -r requirements.txt
streamlit run app.py
```

## Author

Rahma Ras · DATA 606 Capstone · [GitHub](https://github.com/RahmaRas) · [Live App](https://rasrahma06-rahmaras-er-predictor.hf.space)
