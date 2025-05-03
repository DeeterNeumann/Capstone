from PyQt6.QtWidgets import (
    QVBoxLayout,
    QTableView,
    QWidget,
    QHeaderView,
)
from PyQt6.QtGui import (
    QStandardItemModel,
)

class CARProductTab(QWidget):
    def __init__(self):
        super().__init__()

        self.model = QStandardItemModel(10, 5)
        self.model.setHorizontalHeaderLabels([
            'patient_id',
            'product_id',
            'product_name',
            'manufacturer',
            'target_antigen'
        ])
        self.table = QTableView()
        self.table.setModel(self.model)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

        layout = QVBoxLayout()
        layout.addWidget(self.table)

        self.setLayout(layout)