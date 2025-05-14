from sqlalchemy import Column, Integer, String, ForeignKey, Table, Float
from sqlalchemy.orm import relationship, backref
# from sqlalchemy.ext.declarative import declarative_base
from models import Base

# Base = declarative_base()

# # # Many-to-Many Relationships???
# car_product = Table(
#     "CAR_product",
#     Base.metadata,
#     Column("patient_id", Integer,)
# )

# # # *****Creating relationships???

class CARProduct(Base):
    __tablename__ = "CAR_product"
    product_id = Column(Integer, primary_key = True)
    patient_id = Column(Integer, ForeignKey())
    product_name = Column(String)
    manufacturer = Column(String)
    target_antigen = Column(String)

class Diagnosis(Base):
    __tablename__ = "Diagnosis"
    diagnosis_id = Column(Integer, primary_key = True)
    patient_id = Column(Integer, ForeignKey())
    diagnosis_name = Column(String)

### LabValues is a One-to-Many Relationship (each patient can have many lab values, but each lab order belongs to one patient)
class LabValues(Base):
    __tablename__ = "Lab Values"
    patient_id = Column(Integer)
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

class Outcomes(Base):
    __tablename__ = "Outcomes"
    patient_id = Column(Integer)
    outcome_id = Column(Integer)
    therapy_id = Column(Integer)
    response = Column(String)
    date_assessed = Column(Integer)
    relapse_date = Column(Integer)
    death_date = Column(Integer)

class PatientData(Base):
    __tablename__ = "Patient Data"
    patient_id = Column(Integer, primary_key = True)
    mrn = Column(Integer)
    first_name = Column(String)
    last_name = Column(String)
    dob = Column(Integer)
    sex = Column(String)
    diagnosis_id = Column(Integer)

class SideEffects(Base):
    __tablename__ = "Side Effects"
    patient_id = Column(Integer)
    side_effect_id = Column(Integer)
    therapy_id = Column(Integer)
    side_effect_type = Column(String)
    grade = Column(String)
    onset_date = Column(Integer)
    resolution_date = Column(Integer)
    management = Column(String)

class TherapyDetails(Base):
    __tablename__ = "Therapy Details"
    patient_id = Column(Integer)
    therapy_id = Column(Integer)
    product_id = Column(Integer)
    infusion_date = Column(Integer)
    lymphodepletion_regimen = Column(String)
    cell_dose = Column(Float)

