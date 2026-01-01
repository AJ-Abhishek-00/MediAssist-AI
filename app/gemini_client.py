import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use a valid model name
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_explanation(condition: str, medicines: list[str]) -> str:
    prompt = f"""
Condition: {condition}
Suggested Medicines: {", ".join(medicines)}

Explain the condition in simple terms.
Explain safe usage of medicines.
Mention precautions.
Clearly say when to consult a doctor.
Add a disclaimer that this is not medical advice.
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception:
        return (
            "AI explanation is temporarily unavailable. "
            "Please consult a qualified healthcare professional."
        )
