from sqlalchemy import Column, Integer, String, ForeignKey, Table, Float
from sqlalchemy.orm import relationship, backref
# from sqlalchemy.ext.declarative import declarative_base
from models import Base

# Base = declarative_base()

class Outcomes(Base):
    __tablename__ = "Outcomes"
    outcome_id = Column(Integer, primary_key = True)
    patient_id = Column(Integer, ForeignKey("Patient_Data.patient_id"))
    therapy_id = Column(Integer)
    response = Column(String)
    date_assessed = Column(Integer)
    relapse_date = Column(Integer)
    death_date = Column(Integer)