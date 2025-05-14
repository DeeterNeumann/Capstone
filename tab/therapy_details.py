from PyQt6.QtWidgets import (
    QVBoxLayout,
    QTableView,
    QWidget,
    QHeaderView
)
from PyQt6.QtGui import (
    QStandardItemModel,
)

class TherapyDetailsTab(QWidget):
    def __init__(self):
        super().__init__()

        self.model = QStandardItemModel(10, 6)
        self.model.setHorizontalHeaderLabels([
            'patient_id',
            'therapy_id',
            'product_id',
            'infusion_date',
            'lymphodepletion_regimen',
            'cell_dose'
        ])
        self.table = QTableView()
        self.table.setModel(self.model)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

        layout = QVBoxLayout()
        layout.addWidget(self.table)

        self.setLayout(layout)