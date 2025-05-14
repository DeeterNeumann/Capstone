from PyQt6.QtWidgets import (
    QVBoxLayout,
    QTableView,
    QWidget,
    QHeaderView
)
from PyQt6.QtGui import (
    QStandardItemModel,
)

class OutcomesTab(QWidget):
    def __init__(self):
        super().__init__()

        self.model = QStandardItemModel(10, 7)
        self.model.setHorizontalHeaderLabels([
            'patient_id', 
            'outcome_id',
            'therapy_id',
            'response',
            'date_assessed',
            'relapse_date',
            'death_date'
        ])
        self.table = QTableView()
        self.table.setModel(self.model)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

        layout = QVBoxLayout()
        layout.addWidget(self.table)

        self.setLayout(layout)