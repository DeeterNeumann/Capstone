from sqlalchemy import Column, Integer, String, ForeignKey, Table, Float, insert
from sqlalchemy.orm import relationship, backref, sessionmaker
from database.database_connection import Base, engine
from model.patient_model import PatientData
from model.patient_therapy_model import patient_therapy


# junction table 
class CART(Base):
    __tablename__ = "CAR_T_Cells"
    car_t_id = Column(Integer, primary_key = True)
    car_t_cell = Column(String)

    # patients = relationship("PatientData", secondary = patient_therapy, back_populates = "car_t_therapies")