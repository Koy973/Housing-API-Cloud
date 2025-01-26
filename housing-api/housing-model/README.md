# Housing Price Prediction Model

## Prérequis
- Docker
- Docker Compose

## Lancement du Projet

Pour démarrer le projet, exécutez :

```bash
docker-compose up --build
```

Cette commande va :
- Construire les images nécessaires
- Entraîner automatiquement le modèle
- Lancer l'API de prédiction

L'API sera accessible à l'adresse : http://localhost:8001

### Exemple d'Utilisation de l'API

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "longitude": -122.23,
    "latitude": 37.88,
    "housing_median_age": 41,
    "total_rooms": 880,
    "total_bedrooms": 129,
    "population": 322,
    "households": 126,
    "median_income": 8.3252,
    "ocean_proximity_INLAND": 0,
    "ocean_proximity_NEAR BAY": 1
  }' \
  http://localhost:8001/predict
```

### Arrêt du Projet

Pour arrêter les services :

```bash
docker-compose down
```
