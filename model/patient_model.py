from sqlalchemy import Column, Integer, String, ForeignKey, Table, Float, Date
from sqlalchemy.orm import relationship, backref, sessionmaker
from database.database_connection import Base, engine
from model.patient_therapy_model import patient_therapy

class PatientData(Base):
    __tablename__ = "Patient_Data"
    patient_id = Column(Integer, primary_key = True)
    mrn = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    dob = Column(Date)
    bio_sex = Column(String)

    lab_values = relationship("LabValues", back_populates = "patient", cascade="all, delete-orphan")
    car_t_therapies = relationship("CART", secondary = patient_therapy, back_populates = "patients")
    