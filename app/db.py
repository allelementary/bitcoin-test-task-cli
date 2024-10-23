from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import settings

DATABASE_URL = (
    f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}"
    f"@{settings.POSTGRES_SERVER}:5432/{settings.POSTGRES_DB}"
)

# Create the engine
engine = create_engine(DATABASE_URL)

# Create a session factory
Session = sessionmaker(bind=engine)
session = Session()

meta_data = MetaData()
Base = declarative_base(metadata=meta_data)
