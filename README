1 - Installation :

	Clonez ce dépôt et placez-vous dans le dossier housing-api.
	Installez les dépendances (via Poetry ou pip).

2 - Configuration :

	Créez un fichier .env dans housing-api/ avec vos identifiants PostgreSQL, par exemple :

	DB_HOST=localhost
	DB_PORT=5432
	DB_USER=ko
	DB_PASSWORD=mypassword
	DB_NAME=mydatabase_cloud_project
	Assurez-vous que PostgreSQL est démarré et que la base existe.

3- Migrations :

	Appliquez les migrations avec Alembic :
	bash

	alembic upgrade head

4 - Lancement :

	Démarrez l’API :
	bash

	uvicorn app.main:app --reload

	Accédez à la documentation sur http://127.0.0.1:8000/docs.

5 - Utilisation :

	POST /houses pour ajouter une nouvelle maison.
	GET /houses pour lister toutes les maisons.










