from sqlalchemy import Column, Integer, String, ForeignKey, Table, Float
from sqlalchemy.orm import relationship, backref
# from sqlalchemy.ext.declarative import declarative_base
from models import Base

# Base = declarative_base()

class SideEffects(Base):
    __tablename__ = "Side Effects"
    patient_id = Column(Integer)
    side_effect_id = Column(Integer, primary_key=True)
    therapy_id = Column(Integer)
    side_effect_type = Column(String)
    grade = Column(String)
    onset_date = Column(Integer)
    resolution_date = Column(Integer)
    management = Column(String)

