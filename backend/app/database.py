from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL: Ensure the URL is loaded securely from an environment variable for production use
import os
from dotenv import load_dotenv

# Load environment variables from a .env file if available
load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@db:5432/polymerdb")

# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

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
