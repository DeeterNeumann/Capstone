from PyQt6.QtWidgets import (
    QVBoxLayout,
    QTableView,
    QWidget,
    QHeaderView
)
from PyQt6.QtGui import (
    QStandardItemModel,
)

class LabValuesTab(QWidget):
    def __init__(self):
        super().__init__()

        self.model = QStandardItemModel(10, 19)
        self.model.setHorizontalHeaderLabels([
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
