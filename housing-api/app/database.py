# app/database.py

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# On charge le contenu du fichier .env
# Par défaut, load_dotenv() va chercher le fichier .env dans le dossier courant
# ou dans le dossier parent si absent (vous pouvez préciser un chemin si besoin).
load_dotenv()

# Récupérer les variables d’environnement
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_NAME = os.getenv("DB_NAME", "mydatabase_cloud_project")

# Construit la chaîne de connexion
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Crée le moteur de connexion
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Crée la Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base est la classe mère des modèles SQLAlchemy
Base = declarative_base()
