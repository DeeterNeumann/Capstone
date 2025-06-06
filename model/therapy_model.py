from sqlalchemy import Column, Integer, String, Float
from database.database_connection import Base

class TherapyDetails(Base):
    __tablename__ = "Therapy_Details"
    therapy_id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    infusion_date = Column(String)
    lymphodepletion_regimen = Column(String)
    cell_dose = Column(Float)