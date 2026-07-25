# 🏦 Loan Approval Prediction using Machine Learning

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-Completed-success?style=for-the-badge)

---

## 📌 Project Overview

Financial institutions process thousands of loan applications every day. Making accurate loan approval decisions is critical to reducing financial risk while ensuring eligible applicants receive loans.

This project develops an **end-to-end Machine Learning Classification Pipeline** to predict whether a loan application will be **Approved** or **Rejected** using applicant information.

The project covers the complete Machine Learning lifecycle, including:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Feature Encoding
- Feature Scaling
- Model Building
- Hyperparameter Tuning
- Model Evaluation
- ROC-AUC Analysis
- Prediction on Unseen Data

---

# 📊 Dataset

**Source:** Kaggle Loan Approval Prediction Dataset

### Features

- Gender
- Married
- Dependents
- Education
- Self Employed
- Applicant Income
- Coapplicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Property Area

**Target Variable**

- Loan Status (Approved / Rejected)

---

# 🔍 Exploratory Data Analysis (EDA)

Performed comprehensive EDA to understand the dataset.

### ✔ Missing Value Analysis

Handled missing values using appropriate imputation techniques.

### ✔ Univariate Analysis

Studied feature distributions using:

- Count Plots
- Histograms
- Boxplots

### ✔ Bivariate Analysis

Key observations:

- Married applicants had higher loan approval rates.
- Graduates received more loan approvals.
- Applicants from Semi-Urban areas showed higher approval rates.
- Self-employed applicants had comparatively lower approval rates.
- Credit History showed the strongest relationship with loan approval.

### ✔ Correlation Analysis

Correlation heatmap indicated **no strong linear relationship** among numerical features.

### ✔ Outlier Detection

Outliers were identified using Boxplots.

Instead of removing them directly, they were retained since they represented genuine high-income applicants rather than data entry errors.

---

# ⚙ Data Preprocessing

The following preprocessing steps were performed:

- Missing Value Imputation
- One-Hot Encoding for Nominal Features
- Ordinal Encoding for Dependents
- Feature Scaling using StandardScaler
- Train-Test Split (80:20)

---

# 🤖 Machine Learning Models

The following classification algorithms were implemented and compared:

- Logistic Regression
- Decision Tree
- Random Forest
- AdaBoost
- Gradient Boosting
- Naive Bayes
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)

---

# 📈 Model Evaluation

Models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- ROC Curve
- ROC-AUC Score

---

# ⚡ Hyperparameter Tuning

RandomizedSearchCV was initially used to tune multiple shortlisted models.

To ensure a fair comparison, each selected model was then tuned individually using its own hyperparameter search space.

Models tuned:

- Logistic Regression
- Random Forest
- AdaBoost
- SVM

---

# 🏆 Final Model Performance

| Metric | Score |
|---------|-------|
| Accuracy | **86.18%** |
| Precision | **84.00%** |
| Recall | **98.82%** |
| ROC-AUC | **0.8483** |

## ✅ Final Selected Model

**Logistic Regression**

---

# 📉 ROC Curve

The ROC Curve demonstrates the classification capability of the final Logistic Regression model.

**ROC-AUC Score:** **0.8483**

The model achieved good discriminative performance in distinguishing approved and rejected loan applications.

> *(Add your ROC Curve image here after uploading it to GitHub.)*

```markdown
![ROC Curve](images/roc_curve.png)
```

---

# 🔮 Prediction on Unseen Data

The trained Logistic Regression model was tested on unseen loan application data.

Example prediction:

- **Loan Approval Probability:** **85.74%**
- **Loan Rejection Probability:** **14.26%**

This demonstrates the model's ability to generalize well to new loan applications.

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

# 📂 Repository Structure

```
Loan-Approval-Prediction/
│
├── Loan_Approval_Prediction.ipynb
├── loan.csv
├── README.md
├── requirements.txt
├── images/
│   ├── roc_curve.png
│   ├── confusion_matrix.png
│   ├── correlation_heatmap.png
│   └── model_comparison.png
└── LICENSE
```

---

# 🚀 Key Skills Demonstrated

✔ Data Cleaning

✔ Exploratory Data Analysis

✔ Missing Value Handling

✔ Feature Engineering

✔ Feature Encoding

✔ Feature Scaling

✔ Classification Algorithms

✔ Hyperparameter Tuning

✔ Model Evaluation

✔ ROC-AUC Analysis

✔ Machine Learning Pipeline

✔ Prediction on Unseen Data

---

# 📌 Future Improvements

- XGBoost
- LightGBM
- CatBoost
- Explainable AI using SHAP
- Streamlit Deployment
- Flask REST API
- Docker Containerization

---

# 👨‍💻 Author

## Dharani Kaligi

**Data Engineer | Aspiring Data Scientist | Machine Learning Enthusiast**

If you found this project useful, don't forget to ⭐ star this repository.
