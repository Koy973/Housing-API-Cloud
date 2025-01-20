from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# On importe Base et l'URL de connexion
from app.database import Base, SQLALCHEMY_DATABASE_URL
# Importer vos modèles pour qu'Alembic détecte les tables
from app.models import House  # ou tout autre modèle

# Config Alembic
config = context.config
fileConfig(config.config_file_name)

# On écrit l'URL dans la config Alembic
config.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URL)

target_metadata = Base.metadata



def run_migrations_offline():
    """Mode 'offline'"""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True, dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Mode 'online'"""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section), prefix="sqlalchemy.", poolclass=pool.NullPool
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
