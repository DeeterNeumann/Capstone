from sqlalchemy import Column, Integer, String, ForeignKey, Table, Float
from sqlalchemy.orm import relationship, backref
# from sqlalchemy.ext.declarative import declarative_base
from models import Base

# Base = declarative_base()

### LabValues is a One-to-Many Relationship (each patient can have many lab values, but each lab order belongs to one patient)
class LabValues(Base):
    __tablename__ = "Lab Values"
    lab_id = Column(Integer, primary_key = True)
    patient_id = Column(Integer, ForeignKey("Patient_Data.patient_id"))
    date = Column(Integer)
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