import pandas as pd
import joblib
import re

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report


# ---------- LOAD DATASET ----------
df = pd.read_csv("phishing_email.csv")

# Use correct columns from your dataset
df = df[['text_combined', 'label']]
df.columns = ['text', 'label']

# Ensure correct types
df['text'] = df['text'].astype(str)
df['label'] = df['label'].astype(int)


# ---------- TEXT CLEANING ----------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", " url ", text)   # replace URLs
    text = re.sub(r"\d+", " ", text)           # remove numbers
    text = re.sub(r"\s+", " ", text)           # normalize spaces
    return text.strip()

df['text'] = df['text'].apply(clean_text)


# ---------- TRAIN / TEST SPLIT ----------
X_train, X_test, y_train, y_test = train_test_split(
    df['text'],
    df['label'],
    test_size=0.2,
    random_state=42,
    stratify=df['label']
)


# ---------- ML PIPELINE ----------
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(
        stop_words="english",
        max_df=0.9,
        min_df=5,
        ngram_range=(1, 2)
    )),
    ("model", LogisticRegression(
        max_iter=1000,
        class_weight="balanced"
    ))
])


# ---------- TRAIN ----------
pipeline.fit(X_train, y_train)


# ---------- EVALUATE ----------
y_pred = pipeline.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%\n")

print("Classification Report:")
print(classification_report(y_test, y_pred))


# ---------- SAVE MODEL ----------
joblib.dump(pipeline, "model.pkl")
print("\nModel saved successfully as model.pkl")
