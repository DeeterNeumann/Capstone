from sqlalchemy import Column, Integer, String, ForeignKey, Table, Float
from sqlalchemy.orm import relationship, backref
# from sqlalchemy.ext.declarative import declarative_base
from models import Base

# Base = declarative_base()

class Diagnosis(Base):
    __tablename__ = "Diagnosis"
    diagnosis_id = Column(Integer, primary_key = True)
    patient_id = Column(Integer, ForeignKey("Patient_Data.patient_id"))
    diagnosis_name = Column(String)