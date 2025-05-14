from sqlalchemy import Column, Integer, String, ForeignKey, Table, Float
from sqlalchemy.orm import relationship, backref
# from sqlalchemy.ext.declarative import declarative_base
from models import Base

# Base = declarative_base()

class CARProduct(Base):
    __tablename__ = "CAR_product"
    patient_id = Column(Integer, ForeignKey("Patient_Data.patient_id"))
    product_id = Column(Integer, primary_key = True)
    product_name = Column(String)
    manufacturer = Column(String)
    target_antigen = Column(String)

# Next step to link to SQLite to represent a row in the database

# anything in this if statement, whatever script you pass in is considered the main script
# allows for running sub files and test things out
# When importing file, will never run because its not the main script

# Python data classes - annotation that keeps from writing "init"

# Read and write data to corresponding to database
# Then wire everything together
# How to edit data
# How to save data (get GUI to trigger the save)