from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from database.database_connection import Base


class LabValues(Base):
    __tablename__ = "Lab_Values"
    lab_id = Column(Integer, primary_key = True)
    patient_id = Column(Integer, ForeignKey("Patient_Data.patient_id"))

    date = Column(String)
    CRP = Column(Float)
    ferritin = Column(Float)
    IL6 = Column(Float)
    WBC = Column(Float)
    Hgb = Column(Float)
    Plt = Column(Float)
    ANC = Column(Float)
    ALC = Column(Float)
    AST = Column(Float)
    ALT = Column(Float)
    tBili = Column(Float)
    BUN = Column(Float)
    sCr = Column(Float)
    PT = Column(Float)
    INR = Column(Float)
    Ddimer = Column(Float)
    fibrinogen = Column(Float)

    patient = relationship("PatientData", back_populates="lab_values")