from fastapi import FastAPI
from pydantic import BaseModel
from detector import detect_phishing_rule, detect_phishing_ml

app = FastAPI(title="Phishing Email Detector API")

class EmailRequest(BaseModel):
    email: str


@app.get("/")
def home():
    return {"message": "Phishing Detector API is running"}


@app.post("/detect")
def detect_rule_based(data: EmailRequest):
    """
    Rule-based phishing detection
    """
    return detect_phishing_rule(data.email)


@app.post("/detect-ml")
def detect_ml_based(data: EmailRequest):
    """
    Machine Learning based phishing detection
    """
    return detect_phishing_ml(data.email)
