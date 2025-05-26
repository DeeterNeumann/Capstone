from sqlalchemy import Column, Integer, String, ForeignKey, Table, Float
from sqlalchemy.orm import relationship, backref
from database.database_connection import Base, engine

class Diagnosis(Base):
    __tablename__ = "Diagnosis"
    diagnosis_id = Column(Integer, primary_key = True)
    patient_id = Column(Integer) #(ForeignKey("Patient_Data.patient_id"))
    diagnosis_name = Column(String)