import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

def main():
    # Charger le dataset nettoyé
    df = pd.read_csv("data/housing_clean.csv")

    # Séparer X, y
    X = df.drop("median_house_value", axis=1)
    y = df["median_house_value"]

    # Encoder la colonne ocean_proximity (elle doit exister)
    if "ocean_proximity" in X.columns:
        X = pd.get_dummies(X, columns=["ocean_proximity"], drop_first=True)

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Modèle
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Évaluation
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"MAE = {mae}")
    print(f"R^2 = {r2}")

    # Créer le dossier model/ si besoin
    os.makedirs("model", exist_ok=True)

    # **Sauvegarder le modèle**
    joblib.dump(model, "model/model.joblib")
    print("Modèle sauvegardé dans model/model.joblib")

    # **Sauvegarder la liste ordonnée des colonnes**
    trained_columns = X_train.columns.tolist()
    joblib.dump(trained_columns, "model/trained_columns.joblib")
    print("Liste des colonnes entraînées sauvegardée dans model/trained_columns.joblib")

if __name__ == "__main__":
    main()
