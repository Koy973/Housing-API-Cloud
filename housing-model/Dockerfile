# Dockerfile

FROM python:3.11-slim

WORKDIR /app

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y build-essential

# Copier les fichiers nécessaires pour Poetry
COPY pyproject.toml poetry.lock ./

# Installer Poetry
RUN pip install --upgrade pip
RUN pip install poetry

# Désactiver la création d'environnements virtuels
RUN poetry config virtualenvs.create false

# Installer les dépendances
RUN poetry install --no-interaction --no-ansi --no-root

# Copier le reste du code (train_model.py, predict_api.py, etc.)
COPY . .

# Créer un dossier pour le modèle si nécessaire
RUN mkdir -p /app/model

# Exposer le port de l'API
EXPOSE 8001
