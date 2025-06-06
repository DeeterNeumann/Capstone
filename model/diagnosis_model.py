from sqlalchemy import Column, Integer, String
from database.database_connection import Base

class Diagnosis(Base):
    __tablename__ = "Diagnosis"
    diagnosis_id = Column(Integer, primary_key = True)
    patient_id = Column(Integer) #(ForeignKey("Patient_Data.patient_id"))
    diagnosis_name = Column(String)