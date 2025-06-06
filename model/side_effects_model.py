from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.database_connection import Base

class SideEffects(Base):
    __tablename__ = "Side_Effects"
    side_effect_id = Column(Integer, primary_key=True)
    patient_id = Column(Integer)
    therapy_id = Column(Integer)
    side_effect_type = Column(String)
    grade = Column(String)
    onset_date = Column(String)
    resolution_date = Column(String)
    management = Column(String)

