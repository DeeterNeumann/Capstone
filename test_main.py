from sqlalchemy import Column, Integer, String, ForeignKey, Table, Float, insert
from sqlalchemy.orm import relationship, backref, sessionmaker
from database.database_connection import Base, engine, init_db
from model.patient_model import PatientData
from model.diagnosis_model import Diagnosis
from model.car_product_model import CARProduct
from model.therapy_model import TherapyDetails
from model.side_effects_model import SideEffects
from model.lab_values_model import LabValues
from model.outcomes_model import Outcome
from model.tx_history_model import TreatmentHistory
from datetime import date

if __name__ == "__main__":
    init_db()
    Session = sessionmaker(bind = engine)
    session = Session()

    d = PatientData(first_name = "Deeter", last_name = "N", mrn = 58389292, dob = "6/19/1986", bio_sex = "male")
    lv1 = LabValues(date = "5/31/2025", IL6 = 3454, patient=d)
    lv2 = LabValues(date = "6/1/2025", IL6 = 6453, patient=d)

    session.add(d)
    session.commit()

    patient = session.query(PatientData).first()
    for lv in patient.lab_values:
        print(f"Date: {lv.date}, IL6: {lv.IL6}")

    session.close()

    # # Creates sql statement
    # patient_data = PatientData(mrn = 348583983, first_name = "john", last_name = "smith", dob = "5/15/1980", bio_sex = "male")
    # patient_diagnosis = Diagnosis(patient_id = 2, diagnosis_name = "DLBCL")
    # product = CARProduct(patient_id = 1, product_name = "liso cel", manufacturer = "BMS", target_antigen = "CD19")
    # therapy_details = TherapyDetails(product_id = 4959493, infusion_date = "5/24/2025", lymphodepletion_regimen = "FluCy", cell_dose = 5.67*10**6)
    # side_effect = SideEffects(patient_id = 848578394, therapy_id = 4839458, side_effect_type = "CRS", grade = "3", onset_date = "04/23/2025", resolution_date = "4/27/2025", management = "dexamethaonse")
    # lab_values = LabValues(patient_id = 57575848, date = "5/25/2025", CRP = 6.3, ferritin = 142, IL6 = 6453, WBC = 4.5, Hgb = 9.8, Plt = 76, ANC = 0.12, ALC = 1.4, AST = 34, ALT = 46, tBili = 1.5, BUN = 42, sCr = 1.1, PT = 11.2, INR = 1.0, Ddimer = 10.4, fibrinogen = 123)
    # outcome = Outcome(patient_id = 49305, therapy_id = 23, response = "CR", date_assessed = "02/24/2025", relapse_date = "N/A")
    # treatment_history = TreatmentHistory(patient_id = 49305, treatment_regimen = "DLBCL", time_before_CAR = 210)
    # # add_patient = insert(PatientData)

    # # session.execute(add_patient, [patient_data])
    # session.add(patient_data) 
    # session.add(patient_diagnosis)
    # session.add(product)
    # session.add(therapy_details)
    # session.add(side_effect)
    # session.add(lab_values)
    # session.add(outcome)
    # session.add(treatment_history)
    # session.commit()

    # all_patient_data = session.query(PatientData).all()
    # all_diagnosis_data = session.query(Diagnosis).all()
    # all_product_data = session.query(CARProduct).all()
    # all_therapy_details = session.query(TherapyDetails).all()
    # all_side_effect_data = session.query(SideEffects).all()
    # all_lab_values_data = session.query(LabValues).all()
    # all_outcomes_data = session.query(Outcome).all()
    # all_treatment_history_data = session.query(TreatmentHistory).all()
    
    # print(all_patient_data)
    # print(all_diagnosis_data)
    # print(all_product_data)
    # print(all_therapy_details)
    # print(all_side_effect_data)
    # print(all_lab_values_data)
    # print(all_outcomes_data)
    # print(all_treatment_history_data)
    
    # session.close()