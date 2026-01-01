from fastapi import FastAPI
from pydantic import BaseModel

from app.symptom_engine import identify_condition
from app.medicine_mapper import get_medicines
from app.gemini_client import generate_explanation


# ✅ FastAPI app MUST be created first
app = FastAPI(title="MediAssist AI")


# ✅ Request schema
class SymptomInput(BaseModel):
    symptoms: list[str]


# ✅ API endpoint
@app.post("/analyze")
def analyze(input: SymptomInput):
    conditions = identify_condition(input.symptoms)

    if not conditions:
        return {
            "condition": "No clear match found",
            "medicines": ["Consult a doctor"],
            "explanation": "Symptoms do not clearly map to a known condition."
        }

    medicines = get_medicines(conditions)

    explanation = generate_explanation(
        ", ".join(conditions),
        medicines
    )

    return {
        "condition": ", ".join(conditions),
        "medicines": medicines,
        "explanation": explanation
    }
