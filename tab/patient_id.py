from PyQt6.QtWidgets import (
    QVBoxLayout,
    QTableView,
    QWidget,
    QHeaderView
)
from PyQt6.QtGui import (
    QStandardItemModel,
    QStandardItem
)

from datetime import date 

from sqlalchemy.orm import sessionmaker
from database.database_connection import engine
from model.patient_model import PatientData

class PatientIdTab(QWidget):
    def __init__(self, status_bar=None):
        super().__init__()

        self.patients = []
        Session = sessionmaker(bind=engine)
        self.session = Session()

        self.status_bar = status_bar

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels([
            'patient_id',
            'mrn',
            'first_name',
            'last_name',
            'dob',
            'biological_sex',
        ])
        self.table = QTableView()
        self.table.setModel(self.model)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)

        self.db_load_data()

        self.model.itemChanged.connect(self.handle_edit)

    def db_load_data(self):
        self.patients = self.session.query(PatientData).all()
        self.patient_lookup = {patient.patient_id: patient for patient in self.patients}

        for patient in self.patients:
            items = [
                QStandardItem(str(patient.patient_id)),
                QStandardItem(patient.mrn),
                QStandardItem(patient.first_name),
                QStandardItem(patient.last_name),
                QStandardItem(patient.dob.strftime("%Y-%m-%d") if patient.dob else ""),
                QStandardItem(patient.bio_sex)
            ]

            for item in items:
                item.setEditable(False)
            self.model.appendRow(items)

    def handle_edit(self, item: QStandardItem):
        
        field_names = [column.name for column in PatientData.__table__.columns] 
        editable_fields = [name for name in field_names if name != "patient_id"]

        row = item.row()
        col = item.column()

        headers = [self.model.horizontalHeaderItem(i).text() for i in range(self.model.columnCount())]

        if col == 0:
            return
        
        field_name = headers[col]

        patient_id_item = self.model.item(row, 0)
        if not patient_id_item:
            return
        
        patient_id = int(patient_id_item.text())

        patient = self.patient_lookup.get(patient_id)
        if not patient:
            print(f"Patient with ID {patient_id} not found.")
            return
        
        new_value = item.text()

        current_value = getattr(patient, field_name)
        if str(current_value) != new_value:
            setattr(patient, field_name, new_value)
            try:
                self.session.commit()
                self.refresh_model()
                if self.status_bar:
                    self.status_bar.showMessage(f"Change saved to Patient ID '{patient_id}': '{field_name}'", 5000)
                    
                print(f"Committed {field_name} = {new_value} for Patient ID {patient_id}")
            except Exception as e:
                self.session.rollback()
                print(f"Failed to save change: {e}")

    def refresh_model(self):
        self.model.clear()
        
        columns = PatientData.__table__.columns
        headers = [column.name for column in columns]
        self.model.setHorizontalHeaderLabels(headers)

        
        patients = self.session.query(PatientData).all()
        for pt in patients:
            row_items = []
            for attr in headers:
                value = getattr(pt, attr)
                if isinstance(value, date):
                    value = value.strftime("%Y-%m-%d")
                item = QStandardItem(str(value) if value is not None else "")
                row_items.append(item)
            self.model.appendRow(row_items)
        self.session.close()
