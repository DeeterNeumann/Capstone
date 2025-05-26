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
from model.lab_values_model import LabValues

class LabValuesTab(QWidget):
    def __init__(self, status_bar=None):
        super().__init__()
        
        self.lab_values = []
        Session = sessionmaker(bind=engine)
        self.session = Session()

        self.status_bar = status_bar

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels([
            'lab_id',
            'patient_id',
            'date',
            'CRP',
            'ferritin',
            'IL-6',
            'WBC',
            'Hgb',
            'Plt',
            'ANC',
            'ALC',
            'AST',
            'ALT',
            'tBili',
            'BUN',
            'sCr',
            'PT',
            'INR',
            'D-dimer',
            'fibrinogen'
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
        self.lab_values = self.session.query(LabValues).all()
        self.lab_value_lookup = {lab_value.lab_id: lab_value for lab_value in self.lab_values}

        for lab_value in self.lab_values:
            items = [
                QStandardItem(str(lab_value.lab_id)),
                QStandardItem(str(lab_value.patient_id)),
                QStandardItem(lab_value.date),
                QStandardItem(str(lab_value.CRP)),
                QStandardItem(str(lab_value.ferritin)),
                QStandardItem(str(lab_value.IL6)),
                QStandardItem(str(lab_value.WBC)),
                QStandardItem(str(lab_value.Hgb)),
                QStandardItem(str(lab_value.Plt)),
                QStandardItem(str(lab_value.ANC)),
                QStandardItem(str(lab_value.ALC)),
                QStandardItem(str(lab_value.AST)),
                QStandardItem(str(lab_value.ALT)),
                QStandardItem(str(lab_value.tBili)),
                QStandardItem(str(lab_value.BUN)),
                QStandardItem(str(lab_value.sCr)),
                QStandardItem(str(lab_value.PT)),
                QStandardItem(str(lab_value.INR)),
                QStandardItem(str(lab_value.Ddimer)),
                QStandardItem(str(lab_value.fibrinogen))
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
            2: "date",
            3: "CRP",
            4: "ferritin",
            5: "IL6",
            6: "WBC",
            7: "Hgb",
            8: "Plt",
            9: "ANC",
            10: "ALC",
            11: "AST",
            12: "ALT",
            13: "tBili",
            14: "BUN",
            15: "sCr",
            16: "PT",
            17: "INR",
            18: "Ddimer",
            19: "fibrinogen"
        }

        field_name = field_map.get(col)
        if field_name is None:
            return

        lab_id_item = self.model.item(row, 0)
        if not lab_id_item:
            return
        
        lab_id = int(lab_id_item.text())
        lab_value = self.lab_value_lookup.get(lab_id)
        
        if not lab_value:
            print(f"Lab Values with ID {lab_id} not found.")
            return
        
        new_value = item.text()

        if getattr(lab_value, field_name) != new_value:
            setattr(lab_value, field_name, new_value)
            try:
                self.session.commit()
                
                if self.status_bar:
                    self.status_bar.showMessage(f"Change saved to Lab ID '{lab_id}': '{field_name}'", 5000)
                    
                print(f"Committed {field_name} = {new_value} for Lab ID {lab_id}")
            except Exception as e:
                self.session.rollback()
                print(f"Failed to save change: {e}")

    def refresh_model(self):
        self.model.clear()
        self.model.setHorizontalHeaderLabels([
            "lab_id",
            "patient_id",
            "date",
            "CRP",
            "ferritin",
            "IL6",
            "WBC",
            "Hgb",
            "Plt",
            "ANC",
            "ALC",
            "AST",
            "ALT",
            "tBili",
            "BUN",
            "sCr",
            "PT",
            "INR",
            "Ddimer",
            "fibrinogen"
        ])
        self.db_load_data()