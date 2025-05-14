# Write patient entry data GUI

# Create class to maintain reference to a connection

# class for controller
# self.connection = db_connection
# # # def create(self, patient_model):
        # self.connection (already aware of connection)



# def create(patient_model, connection to db_connection)
# def read
# def update
# def 


# # # # How to manage a single patient that gets multiple therapies

# Use SQLite to create patient table
# Read and write using patient model to and from patient table (write a script, create controller)
# Wire GUI up to it (take controller and allowing GUI to execute the code)
# SQLite Viewer extension (look inside database without using Python)

from sqlalchemy import create_engine, MetaData, Table
from model.patient_model import PatientData

# metadata = MetaData()

# engine = create_engine("sqlite:///capstone.db", echo = True)

# conn = engine.connect()

# patient_id_table = Table()


# 'patient_id',
# 'mrn',
# 'first_name',
# 'last_name',
# 'dob',
# 'sex',
# 'diagnosis_id'

