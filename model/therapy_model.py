from sqlalchemy import Column, Integer, String, ForeignKey, Table, Float
from sqlalchemy.orm import relationship, backref
from database.database_connection import Base, engine

class TherapyDetails(Base):
    __tablename__ = "Therapy Details"
    therapy_id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    infusion_date = Column(String)
    lymphodepletion_regimen = Column(String)
    cell_dose = Column(Float)