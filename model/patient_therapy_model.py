from sqlalchemy import Table, Column, Integer, ForeignKey

from database.database_connection import Base


patient_therapy = Table(
    'Patient_Therapy',
    Base.metadata,
    Column("patient_id", Integer, ForeignKey("Patient_Data.patient_id")),
    Column("therapy_id", Integer, ForeignKey("CAR_T_Cells.car_t_id"))
)
