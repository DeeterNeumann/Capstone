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
from model.outcomes_model import Outcome

Session = sessionmaker(bind=engine)

class AddOutcome(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Patient Outcome")
        self.session = Session()

        self.layout = QVBoxLayout()
        form = QFormLayout()
                
        self.patient_id = QLineEdit()
        self.therapy_id = QLineEdit()
        self.response = QLineEdit()
        self.date_assessed = QLineEdit()
        self.relapse_date = QLineEdit()

        form.addRow("Patient ID:", self.patient_id)
        form.addRow("Therapy ID:", self.therapy_id)
        form.addRow("Treatment Response:", self.response)
        form.addRow("Date Assessed (MM/DD/YYYY):", self.date_assessed)
        form.addRow("Relapse Date:", self.relapse_date)

        self.layout.addLayout(form)
                
        self.buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Cancel
            | QDialogButtonBox.StandardButton.Ok
        )
        self.buttons.accepted.connect(self.save_outcome)
        self.buttons.rejected.connect(self.reject)

        self.layout.addWidget(self.buttons)
        self.setLayout(self.layout)

    outcome_added = pyqtSignal()

    def save_outcome(self):        
        try:
            new_outcome = Outcome(
                patient_id = self.patient_id.text(),
                therapy_id = self.therapy_id.text(),
                response = self.response.text(),
                date_assessed = self.date_assessed.text(),
                relapse_date = self.relapse_date.text()
            )
                        
            self.session.add(new_outcome)
            self.session.commit()
            QMessageBox.information(self, "Success", "Patient Outcome Added")

            self.outcome_added.emit()
            self.accept()
        except Exception as e:
            self.session.rollback()
            QMessageBox.critical(self, "Error", f"Could not add patient outcome: {e}")

if __name__ == "__main__":
        app = QApplication([])
        add_outcome = AddOutcome()
        add_outcome.show()
        sys.exit(app.exec())