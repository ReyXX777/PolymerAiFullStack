from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
import os
from dotenv import load_dotenv

# Load environment variables from a .env file if available
load_dotenv()

# Database URL: Ensure the URL is loaded securely from an environment variable for production use
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@db:5432/polymerdb")

# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True, pool_size=10, max_overflow=20)

# Configure the session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models
Base = declarative_base()

# Dependency for getting a database session
def get_db():
    """
    Dependency that provides a database session. Used in FastAPI routes for request-scoped sessions.

    Yields:
        session: A database session instance.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Context manager for database sessions
@contextmanager
def session_scope():
    """
    Context manager for handling database sessions with automatic rollback on exceptions.

    Yields:
        session: A database session instance.
    """
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

# Example usage of the session_scope context manager
if __name__ == "__main__":
    with session_scope() as session:
        # Perform database operations here
        print("Database session created and managed successfully.")
