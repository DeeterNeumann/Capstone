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
from model.therapy_model import TherapyDetails

class TherapyDetailsTab(QWidget):
    def __init__(self, status_bar=None):
        super().__init__()

        self.therapy_details = []
        Session = sessionmaker(bind=engine)
        self.session = Session()

        self.status_bar = status_bar

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels([
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

        self.db_load_data()

        self.model.itemChanged.connect(self.handle_edit)

    def db_load_data(self):
        self.therapy_details = self.session.query(TherapyDetails).all()
        self.therapy_details_lookup = {therapy_detail.therapy_id: therapy_detail for therapy_detail in self.therapy_details}

        for therapy_detail in self.therapy_details:
            items = [
                QStandardItem(str(therapy_detail.therapy_id)),
                QStandardItem(str(therapy_detail.product_id)),
                QStandardItem(therapy_detail.infusion_date),
                QStandardItem(therapy_detail.lymphodepletion_regimen),
                QStandardItem(str(therapy_detail.cell_dose))
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
            1: "product_id",
            2: "infusion_date",
            3: "lymphodepletion_regimen",
            4: "cell_dose",
        }

        field_name = field_map.get(col)
        if field_name is None:
            return

        therapy_id_item = self.model.item(row, 0)
        if not therapy_id_item:
            return
        
        therapy_id = int(therapy_id_item.text())
        therapy_detail = self.therapy_details_lookup.get(therapy_id)
        
        if not therapy_detail:
            print(f"Therapy details for {therapy_id} not found.")
            return
        
        new_value = item.text()

        if getattr(therapy_detail, field_name) != new_value:
            setattr(therapy_detail, field_name, new_value)
            try:
                self.session.commit()

                if self.status_bar:
                    self.status_bar.showMessage(f"Change saved to Therapy details '{therapy_id}': '{field_name}'", 5000)
                print(f"Committed {field_name} = {new_value} for {therapy_id}")
            except Exception as e:
                self.session.rollback()
                print(f"Failed to save change: {e}")


    def refresh_model(self):
        self.model.clear()
        self.model.setHorizontalHeaderLabels([
            "therapy_id",
            "product_id",
            "infusion_date",
            "lymphodepletion_regimen",
            "cell_dose",
        ])
        self.db_load_data()