import sys

from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QMessageBox
)

from PyQt6.QtCore import pyqtSignal
from sqlalchemy.orm import sessionmaker
from database.database_connection import engine
from model.therapy_model import TherapyDetails

Session = sessionmaker(bind=engine)

class AddTherapyDetails(QDialog):
        def __init__(self, parent=None):
                super().__init__(parent)
                self.setWindowTitle("Add New Patient")
                self.session = Session()

                self.layout = QVBoxLayout()
                form = QFormLayout()
                
                self.product_id = QLineEdit()
                self.infusion_date = QLineEdit()
                self.lymphodepletion_regimen = QLineEdit()
                self.cell_dose = QLineEdit()

                form.addRow("Product ID:", self.product_id)
                form.addRow("Infusion Date:", self.infusion_date)
                form.addRow("Lymphodepletion Regimen:", self.lymphodepletion_regimen)
                form.addRow("Cell Dose", self.cell_dose)

                self.layout.addLayout(form)
                
                self.buttons = QDialogButtonBox(
                        QDialogButtonBox.StandardButton.Cancel
                        | QDialogButtonBox.StandardButton.Ok
                )
                self.buttons.accepted.connect(self.save_therapy_details)
                self.buttons.rejected.connect(self.reject)

                self.layout.addWidget(self.buttons)
                self.setLayout(self.layout)

        therapy_details_added = pyqtSignal()

        def save_therapy_details(self):
                try:
                        new_details = TherapyDetails(
                                product_id = self.product_id.text(),
                                infusion_date = self.infusion_date.text(),
                                lymphodepletion_regimen = self.lymphodepletion_regimen.text(),
                                cell_dose = self.cell_dose.text(),
                        )
                        self.session.add(new_details)
                        self.session.commit()
                        QMessageBox.information(self, "Success", "Therapy Details Added")

                        self.therapy_details_added.emit()
                        self.accept()
                except Exception as e:
                        self.session.rollback()
                        QMessageBox.critical(self, "Error", f"Could not add new therapy details: {e}")


if __name__ == "__main__":
        app = QApplication([])
        add_therapy_details = AddTherapyDetails()
        add_therapy_details.show()
        sys.exit(app.exec())
