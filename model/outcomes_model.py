from sqlalchemy import Column, Integer, String, ForeignKey, Table, Float
from sqlalchemy.orm import relationship, backref
from database.database_connection import Base, engine

class Outcome(Base):
    __tablename__ = "Outcomes"
    outcome_id = Column(Integer, primary_key = True)
    patient_id = Column(Integer)
    therapy_id = Column(Integer)
    response = Column(String)
    date_assessed = Column(String)
    relapse_date = Column(String)