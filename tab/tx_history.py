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
from model.tx_history_model import TreatmentHistory

class TxHistoryTab(QWidget):
    def __init__(self, status_bar=None):
        super().__init__()

        self.tx_history = []
        Session = sessionmaker(bind=engine)
        self.session = Session()

        self.status_bar = status_bar

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels([
            "history_id",
            'patient_id',
            'treatment_regimen',
            'time_before_CAR'
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
        self.tx_histories = self.session.query(TreatmentHistory).all()
        self.tx_history_lookup = {tx_history.history_id: tx_history for tx_history in self.tx_histories}

        for tx_history in self.tx_histories:
            items = [
                QStandardItem(str(tx_history.history_id)),
                QStandardItem(str(tx_history.patient_id)),
                QStandardItem(tx_history.treatment_regimen),
                QStandardItem(str(tx_history.time_before_CAR))
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
            2: "treatment_regimen",
            3: "time_before_CAR"
        }

        field_name = field_map.get(col)
        if field_name is None:
            return
        
        history_id_item = self.model.item(row, 0)
        if not history_id_item:
            return
        
        history_id = int(history_id_item.text())
        tx_history = self.tx_history_lookup.get(history_id)

        if not tx_history:
            print(f"Treatment History with ID {history_id} not found.")
            return
        
        new_value = item.text()

        if getattr(tx_history,field_name) != new_value:
            setattr(tx_history, field_name, new_value)
            try:
                self.session.commit()

                if self.status_bar:
                    self.status_bar.showMessage(f"Change saved to History ID {history_id}: '{field_name}'", 5000)

                print(f"Committed {field_name} = {new_value} for History ID {history_id}")
            except Exception as e:
                self.session.rollback()
                print(f"Failed to save change: {e}")

    def refresh_model(self):
        self.model.clear()
        self.model.setHorizontalHeaderLabels([
            "history_id",
            "patient_id",
            "treatment_regimen",
            "time_before_CAR"
        ])
        self.db_load_data()