import sys

from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QPushButton,
    QMessageBox,
    QWidget
)

from PyQt6.QtCore import pyqtSignal
from sqlalchemy.orm import sessionmaker
from database.database_connection import engine
from model.car_product_model import CARProduct

Session = sessionmaker(bind=engine)

class AddCARProduct(QDialog):
        def __init__(self, parent=None):
                super().__init__(parent)
                self.setWindowTitle("Add Product")
                self.session = Session()

                self.layout = QVBoxLayout()
                form = QFormLayout()
                
                self.patient_id = QLineEdit()
                self.product_name = QLineEdit()
                self.manufacturer = QLineEdit()
                self.targe_antigen = QLineEdit()

                form.addRow("Patient ID:", self.patient_id)
                form.addRow("Product Name:", self.product_name)
                form.addRow("Manufacturer:", self.manufacturer)
                form.addRow("Target Antigen:", self.targe_antigen)

                self.layout.addLayout(form)
                
                self.buttons = QDialogButtonBox(
                        QDialogButtonBox.StandardButton.Cancel
                        | QDialogButtonBox.StandardButton.Ok
                )
                self.buttons.accepted.connect(self.save_product)
                self.buttons.rejected.connect(self.reject)

                self.layout.addWidget(self.buttons)
                self.setLayout(self.layout)

        product_added = pyqtSignal()

        def save_product(self):
                try:
                        new_product = CARProduct(
                                patient_id = self.patient_id.text(),
                                product_name = self.product_name.text(),
                                manufacturer = self.manufacturer.text(),
                                target_antigen = self.targe_antigen.text(),
                        )
                        self.session.add(new_product)
                        self.session.commit()
                        QMessageBox.information(self, "Success", "New Product Added")

                        self.product_added.emit()
                        self.accept()
                except Exception as e:
                        self.session.rollback()
                        QMessageBox.critical(self, "Error", f"Could not add new product: {e}")

if __name__ == "__main__":
        app = QApplication([])
        add_product = AddCARProduct()
        add_product.show()
        sys.exit(app.exec())