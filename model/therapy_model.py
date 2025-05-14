from sqlalchemy import Column, Integer, String, ForeignKey, Table, Float
from sqlalchemy.orm import relationship, backref
# from sqlalchemy.ext.declarative import declarative_base
from models import Base

# Base = declarative_base()

class TherapyDetails(Base):
    __tablename__ = "Therapy Details"
    patient_id = Column(Integer)
    therapy_id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    infusion_date = Column(Integer)
    lymphodepletion_regimen = Column(String)
    cell_dose = Column(Float)