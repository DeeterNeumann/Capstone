from sqlalchemy import Column, Integer, String, ForeignKey, Table, Float, insert
from sqlalchemy.orm import relationship, backref, sessionmaker
from database.database_connection import Base, engine, init_db
from model.patient_model import PatientData

# if __name__ == "__main__":
#     print("Hello")

# pysimplegui
# PyQT

# look at examples
    # pictures etc
# look at documentation to get familiar (maybe have gallery)
# Review tutorials
# Select GUI application
# Draw out GUI



if __name__ == "__main__":
    init_db()
    Session = sessionmaker(bind = engine)
    session = Session()

    # Creates sql statement
    patient_data = PatientData(mrn = 348583983, first_name = "john", last_name = "smith", dob = "5/15/1980", sex = "male")
    # add_patient = insert(PatientData)

    # session.execute(add_patient, [patient_data])
    session.add(patient_data)
    session.commit()

    all_patient_data = session.query(PatientData).all()
    print(all_patient_data)
    session.close()
