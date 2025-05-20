from sqlalchemy import Column, Integer, String, ForeignKey, Table, Float, insert
from sqlalchemy.orm import relationship, backref, sessionmaker
from database.database_connection import Base, engine

class PatientData(Base):
    __tablename__ = "Patient_Data"
    patient_id = Column(Integer, primary_key = True)
    mrn = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    dob = Column(String)
    sex = Column(String)