import streamlit as st
import requests

st.set_page_config(page_title="MediAssist AI", page_icon="🩺")

st.title("🩺 MediAssist AI")
st.caption("Educational Symptom-to-Medicine Decision Support System")

st.warning("⚠️ This tool is for educational purposes only. Not a medical diagnosis system.")

symptoms_input = st.text_input(
    "Enter symptoms (comma separated)",
    placeholder="fever, headache, body pain"
)

if st.button("Analyze"):
    if not symptoms_input.strip():
        st.error("Please enter symptoms.")
    else:
        symptoms = [s.strip() for s in symptoms_input.split(",")]

        response = requests.post(
            "http://localhost:8000/analyze",
            json={"symptoms": symptoms}
        )

        if response.status_code == 200:
            data = response.json()

            st.subheader("🧠 Possible Condition")
            st.success(data["condition"])

            st.subheader("💊 Suggested Medicines")
            st.write(", ".join(data["medicines"]))

            st.subheader("📘 Explanation")
            st.write(data["explanation"])
        else:
            st.error("Backend server not running.")
