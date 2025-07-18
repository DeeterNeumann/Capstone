from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from database.database_connection import Base

class PatientData(Base):
    __tablename__ = "Patient_Data"
    patient_id = Column(Integer, primary_key = True)
    mrn = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    dob = Column(Date)
    bio_sex = Column(String)

    lab_values = relationship("LabValues", back_populates = "patient", cascade="all, delete-orphan")
    car_t_therapies = relationship("CART", secondary = "Patient_Therapy", back_populates = "patients")
    