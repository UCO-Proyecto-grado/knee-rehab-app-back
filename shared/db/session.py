from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from shared.core.config import settings
from shared.db.base_class import Base

DATABASE_URL = (
    f"postgresql://{settings.database_user}:{settings.database_password}"
    f"@{settings.database_host}:{settings.database_port}/{settings.database_name}"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
