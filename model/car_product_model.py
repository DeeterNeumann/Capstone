from sqlalchemy import Column, Integer, String, ForeignKey, Table, Float
from sqlalchemy.orm import relationship, backref
from database.database_connection import Base, engine

class CARProduct(Base):
    __tablename__ = "CAR_product"
    product_id = Column(Integer, primary_key = True)
    patient_id = Column(Integer)
    product_name = Column(String)
    manufacturer = Column(String)
    target_antigen = Column(String)