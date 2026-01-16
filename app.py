import streamlit as st
import requests

st.set_page_config(page_title="Phishing Detector", layout="centered")
st.title("🔐 Phishing Email Detector")

email = st.text_area("Paste email content here:")

if st.button("Detect"):
    response = requests.post(
        "http://127.0.0.1:8000/detect-ml",
        json={"email": email}
    )

    result = response.json()

    # ✅ HANDLE API ERRORS SAFELY
    if "error" in result:
        st.error(result["error"])
    else:
        if result["label"] == "Phishing":
            st.error(f"🚨 Phishing Detected ({result['confidence']}%)")
        else:
            st.success(f"✅ Safe Email ({result['confidence']}%)")
