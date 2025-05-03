from PyQt6.QtWidgets import (
    QVBoxLayout,
    QTableView,
    QWidget,
    QHeaderView
)
from PyQt6.QtGui import (
    QStandardItemModel,
)

class PatientIdTab(QWidget):
    def __init__(self):
        super().__init__()

        self.model = QStandardItemModel(10, 7)
        self.model.setHorizontalHeaderLabels([
            'patient_id',
            'mrn',
            'first_name',
            'last_name',
            'dob',
            'sex',
            'diagnosis_id'
        ])
        self.table = QTableView()
        self.table.setModel(self.model)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

        layout = QVBoxLayout()
        layout.addWidget(self.table)

        self.setLayout(layout)