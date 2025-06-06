from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.database_connection import Base

# junction table 
class CART(Base):
    __tablename__ = "CAR_T_Cells"
    car_t_id = Column(Integer, primary_key = True)
    car_t_cell = Column(String)

    patients = relationship("PatientData", secondary = "Patient_Therapy", back_populates = "car_t_therapies")