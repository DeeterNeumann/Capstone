from PyQt6.QtWidgets import (
    QVBoxLayout,
    QTableView,
    QWidget,
    QHeaderView
)
from PyQt6.QtGui import (
    QStandardItemModel,
)

class SideEffectsTab(QWidget):
    def __init__(self):
        super().__init__()

        self.model = QStandardItemModel(10, 8)
        self.model.setHorizontalHeaderLabels([
            'patient_id', 
            'side_effect_id',
            'therapy_id',
            'side_effect_type', 
            'grade',
            'onset_date',
            'resolution_date',
            'management'
        ])
        self.table = QTableView()
        self.table.setModel(self.model)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        
        layout = QVBoxLayout()
        layout.addWidget(self.table)

        self.setLayout(layout)