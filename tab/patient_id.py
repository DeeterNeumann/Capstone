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
            'sex',
            # 'diagnosis_id'
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
                QStandardItem(patient.dob),
                QStandardItem(patient.sex)
            ]

            for item in items:
                item.setEditable(True)
            self.model.appendRow(items)

    def handle_edit(self, item: QStandardItem):
        row = item.row()
        col = item.column()

        if col == 0:
            return
        
        field_map = {
            1: "mrn",
            2: "first_name",
            3: "last_name",
            4: "dob",
            5: "sex",
        }

        field_name = field_map.get(col)
        if field_name is None:
            return

        patient_id_item = self.model.item(row, 0)
        if not patient_id_item:
            return
        
        patient_id = int(patient_id_item.text())
        patient = self.patient_lookup.get(patient_id)
        
        if not patient:
            print(f"Patient with ID {patient_id} not found.")
            return
        
        new_value = item.text()

        if getattr(patient, field_name) != new_value:
            setattr(patient, field_name, new_value)
            try:
                self.session.commit()
                
                if self.status_bar:
                    self.status_bar.showMessage(f"Change saved to Patient ID '{patient_id}': '{field_name}'", 5000)
                    
                print(f"Committed {field_name} = {new_value} for Patient ID {patient_id}")
            except Exception as e:
                self.session.rollback()
                print(f"Failed to save change: {e}")

    def refresh_model(self):
        self.model.clear()
        self.model.setHorizontalHeaderLabels([
            "patient_id",
            "mrn",
            "first_name",
            "last_name",
            "dob",
            "sex"
        ])
        self.db_load_data()