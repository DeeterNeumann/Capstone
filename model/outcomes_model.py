from sqlalchemy import Column, Integer, String
from database.database_connection import Base

class Outcome(Base):
    __tablename__ = "Outcomes"
    outcome_id = Column(Integer, primary_key = True)
    patient_id = Column(Integer)
    therapy_id = Column(Integer)
    response = Column(String)
    date_assessed = Column(String)
    relapse_date = Column(String)