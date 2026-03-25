"""Database URL from environment for local dev and deployment."""

import os
from urllib.parse import quote_plus

from dotenv import load_dotenv


def get_database_url() -> str:
    """Return a SQLAlchemy PostgreSQL URL using psycopg (v3).

    If ``DATABASE_URL`` is set (typical on PaaS), it is used after normalizing
    the scheme for SQLAlchemy + psycopg. Otherwise the URL is built from
    ``DB_HOST``, ``DB_PORT``, ``DB_NAME``, ``DB_USER``, and ``DB_PASSWORD``
    (defaults match ``.env.example``).
    """
    load_dotenv()

    url = os.environ.get("DATABASE_URL")
    if url:
        if url.startswith("postgresql+psycopg://"):
            return url
        if url.startswith("postgres://"):
            return "postgresql+psycopg://" + url[len("postgres://") :]
        if url.startswith("postgresql://"):
            return "postgresql+psycopg://" + url[len("postgresql://") :]
        return url

    host = os.environ.get("DB_HOST", "localhost")
    port = os.environ.get("DB_PORT", "5432")
    name = os.environ.get("DB_NAME", "railcast")
    user = os.environ.get("DB_USER", "railcast")
    password = os.environ.get("DB_PASSWORD", "railcast")
    user_enc = quote_plus(user)
    password_enc = quote_plus(password)
    return f"postgresql+psycopg://{user_enc}:{password_enc}@{host}:{port}/{name}"
