from sqlalchemy import Column, Integer, String
from database.database_connection import Base

class TreatmentHistory(Base):
    __tablename__ = "Treatment_History"
    history_id = Column(Integer, primary_key = True)
    patient_id = Column(Integer)
    treatment_regimen = Column(String)
    time_before_CAR = Column(Integer)