from sqlalchemy import Column, Integer, String
from database.database_connection import Base

class CARProduct(Base):
    __tablename__ = "CAR_product"
    product_id = Column(Integer, primary_key = True)
    patient_id = Column(Integer)
    product_name = Column(String)
    manufacturer = Column(String)
    target_antigen = Column(String)