from sqlalchemy import Column, Integer, String, ForeignKey, Table, Float
from sqlalchemy.orm import relationship, backref
# from sqlalchemy.ext.declarative import declarative_base
from models import Base

# Base = declarative_base()

class PatientData(Base):
    __tablename__ = "Patient_Data"
    patient_id = Column(Integer, primary_key = True)
    mrn = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    dob = Column(Integer)
    sex = Column(String)
    diagnosis_id = Column(Integer)

