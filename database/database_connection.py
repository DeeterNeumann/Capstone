from sqlalchemy import create_engine

from sqlalchemy.orm import declarative_base

Base = declarative_base()

engine = create_engine("sqlite:///PyCARTox.db")

def init_db():
    Base.metadata.create_all(engine)