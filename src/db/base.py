from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    f"mssql+pyodbc://{settings.db.master.username}:{settings.db.master.password}@{settings.db.master.server}/"
    f"{settings.db.master.database}?driver={settings.db.master.driver}",
    echo=True,
    encoding='UTF-8'
)

Session = sessionmaker(bind=engine)

Base = declarative_base()
