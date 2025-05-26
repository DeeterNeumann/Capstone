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
from model.diagnosis_model import Diagnosis

class DiagnosisTab(QWidget):
    def __init__(self, status_bar=None):
        super().__init__()

        self.diagnoses = []
        Session = sessionmaker(bind=engine)
        self.session = Session()

        self.status_bar = status_bar

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels([
            'diagnosis_id', 
            'patient_id', 
            'diagnosis_name'
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
        self.diagnoses = self.session.query(Diagnosis).all()
        self.diagnosis_lookup = {diagnosis.diagnosis_id: diagnosis for diagnosis in self.diagnoses}

        for diagnosis in self.diagnoses:
            items = [
                QStandardItem(str(diagnosis.diagnosis_id)),
                QStandardItem(str(diagnosis.patient_id)),
                QStandardItem(diagnosis.diagnosis_name),
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
            1: "patient_id",
            2: "diagnosis_name",
        }

        field_name = field_map.get(col)
        if field_name is None:
            return

        diagnosis_id_item = self.model.item(row, 0)
        if not diagnosis_id_item:
            return
     
        diagnosis_id = int(diagnosis_id_item.text())
        diagnosis = self.diagnosis_lookup.get(diagnosis_id)
        
        if not diagnosis:
            print(f"Patient with Diagnosis ID {diagnosis_id} not found.")
            return
        
        new_value = item.text()

        if getattr(diagnosis, field_name) != new_value:
            setattr(diagnosis, field_name, new_value)
            try:
                self.session.commit()

                if self.status_bar:
                    self.status_bar.showMessage(f"Change saved to Diagnosis ID '{diagnosis_id}': '{field_name}'", 5000)
                print(f"Committed {field_name} = {new_value} for Patient ID {diagnosis_id}")
            except Exception as e:
                self.session.rollback()
                print(f"Failed to save change: {e}")

    def refresh_model(self):
        self.model.clear()
        self.model.setHorizontalHeaderLabels([
            "diagnosis_id", 
            "patient_id",
            "diagnosis_name"
        ])
        self.db_load_data()