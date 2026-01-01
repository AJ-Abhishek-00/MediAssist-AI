import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "condition_medicines.csv"

df = pd.read_csv(DATA_PATH)

def get_medicines(conditions: list[str]) -> list[str]:
    meds = df[df["condition"].isin(conditions)]["medicine"].unique().tolist()

    if not meds:
        return ["Consult a doctor"]

    return meds
