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
from model.tx_history_model import TreatmentHistory

Session = sessionmaker(bind=engine)

class AddTreatmentHistory(QDialog):
        def __init__(self, parent=None):
                super().__init__(parent)
                self.setWindowTitle("Add Treatment History")
                self.session = Session()

                self.layout = QVBoxLayout()
                form = QFormLayout()

                self.patient_id = QLineEdit()
                self.treatment_regimen = QLineEdit()
                self.time_before_CAR = QLineEdit()

                form.addRow("Patient ID:", self.patient_id)
                form.addRow("Treatment Regimen:", self.treatment_regimen)
                form.addRow("Time Before CAR (days):", self.time_before_CAR)

                self.layout.addLayout(form)

                self.buttons = QDialogButtonBox(
                        QDialogButtonBox.StandardButton.Cancel
                        | QDialogButtonBox.StandardButton.Ok
                )
                self.buttons.accepted.connect(self.save_treatment_history)
                self.buttons.rejected.connect(self.reject)

                self.layout.addWidget(self.buttons)
                self.setLayout(self.layout)

        treatment_history_added = pyqtSignal()

        def save_treatment_history(self):
                try:
                        new_treatment_history = TreatmentHistory(
                                patient_id = self.patient_id.text(),
                                treatment_regimen = self.treatment_regimen.text(),
                                time_before_CAR = self.time_before_CAR.text()
                        )
                        self.session.add(new_treatment_history)
                        self.session.commit()
                        QMessageBox.information(self, "Success", "Treatment History Added")

                        self.treatment_history_added.emit()
                        self.accept()
                except Exception as e:
                        self.session.rollback()
                        QMessageBox.critical(self, "Error", f"Could not add treatment history: {e}")

if __name__ == "__main__":
        app = QApplication([])
        add_treatment_history = AddTreatmentHistory()
        add_treatment_history.show()
        sys.exit(app.exec())