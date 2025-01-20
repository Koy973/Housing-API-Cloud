# Housing API

**Housing API** est une API développée en Python avec **FastAPI** qui permet de créer et de récupérer des enregistrements de maisons stockés dans une base de données **PostgreSQL**. Ce guide vous expliquera étape par étape comment installer, configurer et lancer le projet.

---

## Table des Matières

1. [Prérequis](#1-prérequis)
2. [Cloner le Dépôt](#2-cloner-le-dépôt)
3. [Configurer les Variables d’Environnement](#3-configurer-les-variables-denvironnement)
4. [Installer les Dépendances](#4-installer-les-dépendances)
5. [Configurer la Base de Données](#5-configurer-la-base-de-données)
6. [Effectuer les Migrations](#6-effectuer-les-migrations)
7. [Lancer l’Application](#7-lancer-lapplication)
8. [Tester l’API](#8-tester-lapi)
9. [Dépannage](#9-dépannage)
10. [Contribuer](#10-contribuer)
11. [Licence](#11-licence)

---

## 1. Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- **Python 3.9+**
- **Poetry** (gestionnaire de dépendances)
- **PostgreSQL** (local ou distant)
- **Git**
- (Optionnel) **Docker** pour le déploiement conteneurisé

---

## 2. Cloner le Dépôt

1. **Cloner le dépôt GitHub** :
    ```bash
    git clone https://github.com/votre-utilisateur/housing-firstname-lastname.git
    cd housing-firstname-lastname/housing-api
    ```

2. **Naviguer dans le répertoire `housing-api`** :
    ```bash
    cd housing-api
    ```

---

## 3. Configurer les Variables d’Environnement

1. **Créer un fichier `.env`** à la racine du projet (`housing-api/`) :
    ```bash
    touch .env
    ```

2. **Remplir le fichier `.env`** avec les variables suivantes :
    ```ini
    DB_HOST=localhost
    DB_PORT=5432
    DB_USER=ko
    DB_PASSWORD=mypassword
    DB_NAME=mydatabase_cloud_project
    ```

    - **DB_HOST** : Adresse de votre serveur PostgreSQL (ex. `localhost`)
    - **DB_PORT** : Port PostgreSQL (par défaut `5432`)
    - **DB_USER** : Nom d'utilisateur PostgreSQL
    - **DB_PASSWORD** : Mot de passe PostgreSQL
    - **DB_NAME** : Nom de la base de données

3. **Ajouter `.env` au `.gitignore`** pour éviter de committer les informations sensibles :
    ```bash
    echo ".env" >> .gitignore
    ```

---

## 4. Installer les Dépendances

1. **Installer Poetry** (si ce n'est pas déjà fait) :
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

    - **Note** : Ajoutez Poetry à votre `PATH` si nécessaire. Suivez les instructions affichées après l'installation.

2. **Installer les dépendances du projet** :
    ```bash
    poetry install
    ```

3. **Activer l’environnement virtuel de Poetry** :
    ```bash
    poetry shell
    ```

---

## 5. Configurer la Base de Données

1. **Démarrer PostgreSQL** si ce n'est pas déjà fait.

2. **Créer la base de données** :
    - Connectez-vous à PostgreSQL :
        ```bash
        psql -U ko
        ```
    - Créez la base de données :
        ```sql
        CREATE DATABASE mydatabase_cloud_project;
        \q
        ```

    - **Note** : Remplacez `ko` par votre nom d'utilisateur PostgreSQL si nécessaire.

---

## 6. Effectuer les Migrations

Le projet utilise **Alembic** pour gérer les migrations de la base de données.

1. **Initialiser Alembic** *(si ce n’est pas déjà fait)* :
    ```bash
    alembic init alembic
    ```

2. **Configurer Alembic** :
    - Ouvrez `alembic.ini` et assurez-vous que la ligne suivante utilise la variable d'environnement :
        ```ini
        sqlalchemy.url = env:SQLALCHEMY_DATABASE_URL
        ```

    - Modifiez `alembic/env.py` pour charger les modèles et la configuration :
        ```python
        # alembic/env.py

        from logging.config import fileConfig
        from sqlalchemy import engine_from_config
        from sqlalchemy import pool
        from alembic import context

        import os
        from dotenv import load_dotenv

        # Charger les variables d'environnement
        load_dotenv()

        # Importer Base et les modèles
        from app.database import Base, SQLALCHEMY_DATABASE_URL
        from app import models

        # Configuration Alembic
        config = context.config
        config.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URL)
        fileConfig(config.config_file_name)
        target_metadata = Base.metadata

        def run_migrations_offline():
            url = config.get_main_option("sqlalchemy.url")
            context.configure(
                url=url, target_metadata=target_metadata, literal_binds=True, dialect_opts={"paramstyle": "named"},
            )
            with context.begin_transaction():
                context.run_migrations()

        def run_migrations_online():
            connectable = engine_from_config(
                config.get_section(config.config_ini_section),
                prefix="sqlalchemy.",
                poolclass=pool.NullPool,
            )
            with connectable.connect() as connection:
                context.configure(connection=connection, target_metadata=target_metadata)
                with context.begin_transaction():
                    context.run_migrations()

        if context.is_offline_mode():
            run_migrations_offline()
        else:
            run_migrations_online()
        ```

3. **Générer une migration** pour créer la table `houses` :
    ```bash
    alembic revision --autogenerate -m "create houses table"
    ```

4. **Appliquer la migration** :
    ```bash
    alembic upgrade head
    ```

    - Cela créera la table `houses` dans votre base de données PostgreSQL.

---

## 7. Lancer l’Application

1. **Démarrer le serveur FastAPI avec Uvicorn** :
    ```bash
    uvicorn app.main:app --reload
    ```

    - **`app.main:app`** : Indique à Uvicorn d'utiliser l'instance `app` définie dans `app/main.py`.
    - **`--reload`** : Active le rechargement automatique lors de modifications du code (utile en développement).

2. **Vérifier que le serveur fonctionne** :
    - Ouvrez votre navigateur et accédez à [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    - Vous devriez voir la documentation interactive générée par **FastAPI** (Swagger UI).

---

## 8. Tester l’API

Vous pouvez tester l’API directement via la documentation interactive ou en utilisant des outils comme **curl** ou **Postman**.

### 8.1. Créer une Nouvelle Maison (POST /houses)

1. **Endpoint** : `POST /houses`
2. **Exemple de Payload JSON** :
    ```json
    {
      "longitude": -122.23,
      "latitude": 37.88,
      "housing_median_age": 41,
      "total_rooms": 880,
      "total_bedrooms": 129,
      "population": 322,
      "households": 126,
      "median_income": 8.3252,
      "median_house_value": 452600.0,
      "ocean_proximity": "NEAR BAY"
    }
    ```
3. **Réponse Attendue** :
    ```json
    {
      "id": 1,
      "longitude": -122.23,
      "latitude": 37.88,
      "housing_median_age": 41,
      "total_rooms": 880,
      "total_bedrooms": 129,
      "population": 322,
      "households": 126,
      "median_income": 8.3252,
      "median_house_value": 452600.0,
      "ocean_proximity": "NEAR BAY"
    }
    ```

### 8.2. Récupérer Toutes les Maisons (GET /houses)

1. **Endpoint** : `GET /houses`
2. **Réponse Attendue** :
    ```json
    [
      {
        "id": 1,
        "longitude": -122.23,
        "latitude": 37.88,
        "housing_median_age": 41,
        "total_rooms": 880,
        "total_bedrooms": 129,
        "population": 322,
        "households": 126,
        "median_income": 8.3252,
        "median_house_value": 452600.0,
        "ocean_proximity": "NEAR BAY"
      },
      ...
    ]
    ```

---

## 9. Dépannage

- **Erreur de Connexion à la Base de Données** :
    - Vérifiez les valeurs dans votre fichier `.env` (DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME).
    - Assurez-vous que PostgreSQL est en cours d'exécution et que la base de données spécifiée existe.

- **Problèmes de Migration Alembic** :
    - Assurez-vous que `alembic/env.py` est correctement configuré pour charger `SQLALCHEMY_DATABASE_URL`.
    - Vérifiez que vos modèles dans `app/models.py` sont correctement définis.

- **Problèmes avec les Dépendances** :
    - Assurez-vous d'avoir activé l'environnement virtuel Poetry (`poetry shell`).
    - Réinstallez les dépendances si nécessaire :
        ```bash
        poetry install
        ```

- **Afficher les Requêtes SQL** :
    - Vérifiez que `echo=True` est bien configuré dans `create_engine` dans `app/database.py` pour voir les requêtes SQL dans la console.

---

## 10. Contribuer

Les contributions sont les bienvenues ! Pour contribuer :

1. **Fork** ce dépôt.
2. **Créez une branche** pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`).
3. **Committez** vos changements (`git commit -m 'Add some AmazingFeature'`).
4. **Pushez** la branche (`git push origin feature/AmazingFeature`).
5. **Ouvrez une Pull Request**.

---

## 11. Licence

Ce projet est sous licence **MIT**. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

**Merci d’avoir utilisé Housing API !**  
N’hésitez pas à ouvrir des issues ou des pull requests si vous avez des suggestions ou des améliorations à proposer.

