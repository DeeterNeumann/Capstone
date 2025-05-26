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
from model.car_product_model import CARProduct

class CARProductTab(QWidget):
    def __init__(self, status_bar=None):
        super().__init__()
        
        self.car_products = []
        Session = sessionmaker(bind=engine)
        self.session = Session()

        self.status_bar = status_bar

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels([
            'product_id',
            'patient_id',
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

        self.db_load_data()

        self.model.itemChanged.connect(self.handle_edit)

    
    def db_load_data(self):
        self.products = self.session.query(CARProduct).all()
        self.product_lookup = {product.product_id: product for product in self.products}

        for product in self.products:
            items = [
                QStandardItem(str(product.product_id)),
                QStandardItem(str(product.patient_id)),
                QStandardItem(product.product_name),
                QStandardItem(product.manufacturer),
                QStandardItem(product.target_antigen),
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
            2: "product_name",
            3: "manufacturer",
            4: "target_antigen",
        }

        field_name = field_map.get(col)
        if field_name is None:
            return

        product_id_item = self.model.item(row, 0)
        if not product_id_item:
            return
        
        product_id = int(product_id_item.text())
        product = self.product_lookup.get(product_id)
        
        if not product:
            print(f"Patient with Product ID {product_id} not found.")
            return
        
        new_value = item.text()

        if getattr(product, field_name) != new_value:
            setattr(product, field_name, new_value)
            try:
                self.session.commit()

                if self.status_bar:
                    self.status_bar.showMessage(f"Change saved to Patient ID '{product_id}': '{field_name}'", 5000)
                print(f"Committed {field_name} = {new_value} for Patient ID {product_id}")
            except Exception as e:
                self.session.rollback()
                print(f"Failed to save change: {e}")

    def refresh_model(self):
        self.model.clear()
        self.model.setHorizontalHeaderLabels([
            "patient_id",
            "product_name",
            "manufacturer",
            "target_antigen",
        ])
        self.db_load_data()