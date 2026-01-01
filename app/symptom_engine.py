import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "symptoms_conditions.csv"

df = pd.read_csv(DATA_PATH)

# Normalize CSV text
df["symptom"] = df["symptom"].str.lower().str.strip()

def identify_condition(symptoms: list[str]) -> list[str]:
    symptoms = [s.lower().strip() for s in symptoms]

    matched = df[df["symptom"].isin(symptoms)]

    if matched.empty:
        return []

    return matched["condition"].value_counts().index.tolist()
