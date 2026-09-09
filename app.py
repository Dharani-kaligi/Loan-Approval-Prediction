import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

model = joblib.load("loan_logistic_model.pkl")
scaler = joblib.load("scaler.pkl")


class LoanInput(BaseModel):
    Dependents: int
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    Gender_Male: int
    Married_Yes: int
    Education_Not_Graduate: int
    Self_Employed_Yes: int
    Property_Area_Semiurban: int
    Property_Area_Urban: int


@app.get("/")
def home():
    return {"message": "Loan Approval Prediction API is running"}


@app.post("/predict")
def predict(data: LoanInput):

    features = np.array([[
        data.Dependents,
        data.ApplicantIncome,
        data.CoapplicantIncome,
        data.LoanAmount,
        data.Loan_Amount_Term,
        data.Credit_History,
        data.Gender_Male,
        data.Married_Yes,
        data.Education_Not_Graduate,
        data.Self_Employed_Yes,
        data.Property_Area_Semiurban,
        data.Property_Area_Urban
    ]])

    scaled_features = scaler.transform(features)

    prediction = model.predict(scaled_features)[0]

    result = "Approved" if prediction == 1 else "Not Approved"

    return {
        "prediction": int(prediction),
        "loan_status": result
    }