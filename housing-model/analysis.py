# analysis.py
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("TkAgg")  # Pour éviter l'erreur 'tostring_rgb' sous PyCharm
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # 1. Charger le dataset initial
    df = pd.read_csv("data/housing.csv")

    # 2. Aperçu
    print(df.head())
    print(df.info())
    print(df.describe())

    # 3. Vérifier les valeurs manquantes
    missing_values = df.isna().sum()
    print("Valeurs manquantes par colonne :")
    print(missing_values)

    # 4. Gérer les valeurs manquantes : exemple, on supprime les NaN dans total_bedrooms
    df.dropna(subset=["total_bedrooms"], inplace=True)

    # 5. Ignorer ocean_proximity pour la corrélation (mais on la conserve dans le DataFrame final)
    df_num = df.drop(columns=["ocean_proximity"])

    # 6. Visualiser la matrice de corrélation
    plt.figure(figsize=(10,8))
    sns.heatmap(df_num.corr(), annot=True, cmap="viridis")
    plt.title("Matrice de corrélation (variables numériques uniquement)")
    plt.show()

    # 7. Gérer les outliers sur median_house_value (exemple : on retire le top 1%)
    upper_limit = df_num["median_house_value"].quantile(0.99)
    df = df[df["median_house_value"] < upper_limit]

    # 8. Sauvegarder le dataset nettoyé
    df.to_csv("data/housing_clean.csv", index=False)
    print("Dataset nettoyé et sauvegardé dans data/housing_clean.csv")

if __name__ == "__main__":
    main()
