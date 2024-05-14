#Source: https://stackoverflow.com/questions/64236572/fastapi-typeerror-object-of-type-modelmetaclass-is-not-json-serializable
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = os.environ["POSTGRES_LINK"]
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()