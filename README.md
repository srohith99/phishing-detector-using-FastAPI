# 🔐 Phishing Email Detector (FastAPI + Machine Learning)

A cybersecurity project that detects phishing emails using
rule-based analysis and a Machine Learning model trained on a real Kaggle dataset.

## 🧩 What This Project Does

- Accepts email content as input
- Detects phishing using:
  - Rule-based heuristics
  - Machine Learning (TF-IDF + Logistic Regression)
- Returns prediction with confidence score
- Provides REST API and web UI


## 🛠 Tech Stack

- Python 3.13
- FastAPI (Backend API)
- Scikit-learn (ML model)
- Pandas (Data handling)
- Joblib (Model persistence)
- Streamlit (Frontend UI)


## 📁 Project Structure

phishing-detector/
├── main.py
├── detector.py
├── ml_train.py
├── app.py
├── model.pkl
├── phishing_email.csv
├── requirements.txt



## ▶️ Step-by-Step Setup & Run (Follow in Order)

### Step 1 — Open Terminal

mkdir phishing-detector
cd phishing-detector

### Step 2 — Create & Activate Virtual Environment
python -m venv venv
venv\Scripts\activate

### Step 3 — Install Dependencies

pip install -r requirements.txt

### Step 4 — Train the Machine Learning Model

python ml_train.py
✔ This creates model.pkl
✔ Model trained using Kaggle dataset

### Step 5 — Start FastAPI Backend

python -m uvicorn main:app --reload
API: http://127.0.0.1:8000

Docs: http://127.0.0.1:8000/docs

### Step 6 — Start Streamlit Frontend (New Terminal)

venv\Scripts\activate
streamlit run app.py

✔ Browser UI opens automatically

📡 API Endpoints
POST /detect     → Rule-based phishing detection
POST /detect-ml  → Machine Learning detection

🧪 Example Input
json

{
  "email": "URGENT! Verify your bank account now http://bit.ly/xyz"
}

✅ Example Output

{
  "label": "Phishing",
  "confidence": 98
}

### 📌 Use Cases
Cybersecurity learning

Internship / portfolio project

Email security systems

FastAPI + ML integration demo

### 🚀 Future Enhancements
URL reputation analysis

Sender domain verification

Email header inspection

Cloud deployment (Render / Railway)

Advanced ML explainability
