import joblib
import pandas as pd
from fastapi import FastAPI

app = FastAPI()

# Charger le modèle et la liste de colonnes
model = joblib.load("model/model.joblib")
trained_columns = joblib.load("model/trained_columns.joblib")

@app.post("/predict")
def predict(data: dict):
    """
    data est un JSON contenant les features nécessaires au modèle.
    Ex.:
    {
      "longitude": -122.23,
      "latitude": 37.88,
      "housing_median_age": 41,
      "total_rooms": 880,
      "total_bedrooms": 129,
      "population": 322,
      "households": 126,
      "median_income": 8.3252,
      "ocean_proximity_INLAND": 0,
      "ocean_proximity_NEAR BAY": 1,
      ...
    }
    """
    # Convertir le dict en DataFrame
    X_input = pd.DataFrame([data])

    # Réindexer pour forcer l'ordre (et la présence) des colonnes
    # Les colonnes manquantes seront comblées par 0
    X_input = X_input.reindex(columns=trained_columns, fill_value=0)

    # Prédiction
    prediction = model.predict(X_input)[0]
    return {"prediction": float(prediction)}
