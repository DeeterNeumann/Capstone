from sqlalchemy import create_engine
from models import Base
from model.car_product_model import CARProduct
from model.diagnosis_model import Diagnosis
from model.lab_values_model import LabValues
from model.outcomes_model import Outcomes
from model.patient_model import PatientData
from model.side_effects_model import SideEffects
from model.therapy_model import TherapyDetails

engine = create_engine("sqlite:///PyCARTox.db")

Base.metadata.create_all(engine)



