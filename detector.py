import re
import joblib
from pathlib import Path

# ---------- LOAD ML MODEL SAFELY ----------
MODEL_PATH = Path("model.pkl")

ml_model = None
if MODEL_PATH.exists():
    ml_model = joblib.load(MODEL_PATH)


# ---------- RULE-BASED DETECTION ----------
def detect_phishing_rule(email_text: str):
    email_text = email_text.lower()
    score = 0
    reasons = []

    # Keywords
    phishing_keywords = [
        "urgent", "verify", "click here", "password",
        "bank", "login", "otp", "account suspended", "confirm"
    ]

    for word in phishing_keywords:
        if word in email_text:
            score += 1
            reasons.append(f"Keyword detected: {word}")

    # URL detection
    urls = re.findall(r"http[s]?://\S+", email_text)
    if urls:
        score += 2
        reasons.append("Contains URL")

    # URL shorteners
    shorteners = ["bit.ly", "tinyurl", "t.co"]
    for s in shorteners:
        if s in email_text:
            score += 2
            reasons.append("Suspicious short URL")

    # Special characters
    special_chars = re.findall(r"[!$%&*]", email_text)
    if len(special_chars) >= 3:
        score += 1
        reasons.append("Excessive special characters")

    confidence = min(score * 15, 100)

    if score >= 4:
        label = "Phishing"
    else:
        label = "Safe"

    return {
        "label": label,
        "confidence": confidence,
        "reasons": reasons
    }


# ---------- ML-BASED DETECTION ----------
def detect_phishing_ml(email_text: str):
    if ml_model is None:
        return {"error": "ML model not found"}

    prediction = ml_model.predict([email_text])[0]
    probability = ml_model.predict_proba([email_text])[0][1]

    if prediction == 0:
        probability = 1 - probability

    return {
        "label": "Phishing" if prediction == 1 else "Safe",
        "confidence": int(probability * 100)
    }

