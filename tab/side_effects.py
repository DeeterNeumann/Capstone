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
from model.side_effects_model import SideEffects


class SideEffectsTab(QWidget):
    def __init__(self, status_bar=None):
        super().__init__()

        self.side_effects = []
        Session = sessionmaker(bind=engine)
        self.session = Session()

        self.status_bar = status_bar

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels([ 
            'side_effect_id',
            'patient_id',
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

        self.db_load_data()

        self.model.itemChanged.connect(self.handle_edit)


    def db_load_data(self):
        self.side_effects = self.session.query(SideEffects).all()
        self.side_effect_lookup = {side_effect.side_effect_id: side_effect for side_effect in self.side_effects}

        for side_effect in self.side_effects:
            items = [
                QStandardItem(str(side_effect.side_effect_id)),
                QStandardItem(str(side_effect.patient_id)),
                QStandardItem(str(side_effect.therapy_id)),
                QStandardItem(side_effect.side_effect_type),
                QStandardItem(side_effect.grade),
                QStandardItem(side_effect.onset_date),
                QStandardItem(side_effect.resolution_date),
                QStandardItem(side_effect.management)
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
            3: "side_effect_type",
            4: "grade",
            5: "onset_date",
            6: "resolution_date",
            7: "management"
        }

        field_name = field_map.get(col)
        if field_name is None:
            return

        side_effect_item = self.model.item(row, 0)
        if not side_effect_item:
            return
        
        side_effect_id = int(side_effect_item.text())
        side_effect = self.side_effect_lookup.get(side_effect_id)
        
        if not side_effect:
            print(f"Side Effect with ID {side_effect_id} not found.")
            return
        
        new_value = item.text()

        if getattr(side_effect, field_name) != new_value:
            setattr(side_effect, field_name, new_value)
            try:
                self.session.commit()
                
                if self.status_bar:
                    self.status_bar.showMessage(f"Change saved to Side Effect ID '{side_effect_id}': '{field_name}'", 5000)
                    
                print(f"Committed {field_name} = {new_value} for Side Effect ID {side_effect_id}")
            except Exception as e:
                self.session.rollback()
                print(f"Failed to save change: {e}")


    def refresh_model(self):
        self.model.clear()
        self.model.setHorizontalHeaderLabels([
            "side_effect_id"
            "patient_id",
            "therapy_id",
            "side_effect_type",
            "grade",
            "onset_date",
            "resolution_date",
            "management"
        ])
        self.db_load_data()