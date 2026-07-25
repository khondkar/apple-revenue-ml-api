from pathlib import Path

import joblib
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = PROJECT_ROOT / "models" / "apple_revenue_model.joblib"
FEATURES_PATH = PROJECT_ROOT / "models" / "apple_revenue_features.joblib"


model = joblib.load(MODEL_PATH)
feature_columns = joblib.load(FEATURES_PATH)


def generate_prediction(feature_values: dict[str, float]) -> float:
    input_data = pd.DataFrame(
        [feature_values],
        columns=feature_columns,
    )

    prediction = model.predict(input_data)[0]

    return round(float(prediction), 4)
