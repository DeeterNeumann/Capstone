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
from model.outcomes_model import Outcome

class OutcomesTab(QWidget):
    def __init__(self, status_bar=None):
        super().__init__()

        self.outcomes = []
        Session = sessionmaker(bind=engine)
        self.session = Session()

        self.status_bar = status_bar

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels([ 
            'outcome_id',
            'patient_id',
            'therapy_id',
            'response',
            'date_assessed',
            'relapse_date',
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
        self.outcomes = self.session.query(Outcome).all()
        self.outcome_lookup = {outcome.outcome_id: outcome for outcome in self.outcomes}

        for outcome in self.outcomes:
            items = [
                 QStandardItem(str(outcome.outcome_id)),
                 QStandardItem(str(outcome.patient_id)),
                 QStandardItem(str(outcome.therapy_id)),
                 QStandardItem(outcome.response),
                 QStandardItem(outcome.date_assessed),
                 QStandardItem(outcome.relapse_date)
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
            2: "therapy_id",
            3: "response",
            4: "date_assessed",
            5: "relapse_date"
        }

        field_name = field_map.get(col)
        if field_name is None:
            return
        
        outcome_id_item = self.model.item(row, 0)
        if not outcome_id_item:
            return
        
        outcome_id = int(outcome_id_item.text())
        outcome = self.outcome_lookup.get(outcome_id)

        if not outcome:
            print(f"Outcome with ID {outcome_id} not found.")
            return
        
        new_value = item.text()

        if getattr(outcome, field_name) != new_value:
            setattr(outcome, field_name, new_value)
            try:
                self.session.commit()
                if self.status_bar:
                    self.status_bar.showMessage(f"Change saved to Outcome ID '{outcome_id}': '{field_name}'", 5000)

                print(f"Committed {field_name} = {new_value} for Outcome ID {outcome_id}")
            except Exception as e:
                self.session.rollback()
                print(f"Failed to save change: {e}")

    def refresh_model(self):
        self.model.clear()
        self.model.setHorizontalHeaderLabels([
            "outcome_id",
            "patient_id",
            "therapy_id",
            "response",
            "date_assessed",
            "relapse_date"
        ])
        self.db_load_data()