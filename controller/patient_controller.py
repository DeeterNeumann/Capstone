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
from model.patient_model import PatientData

Session = sessionmaker(bind=engine)

class AddPatient(QDialog):
        def __init__(self, parent=None):
                super().__init__(parent)
                self.setWindowTitle("Add New Patient")
                self.session = Session()

                self.layout = QVBoxLayout()
                form = QFormLayout()
                
                self.mrn = QLineEdit()
                self.first_name = QLineEdit()
                self.last_name = QLineEdit()
                self.dob = QLineEdit()
                self.sex = QLineEdit()

                form.addRow("MRN:", self.mrn)
                form.addRow("First Name:", self.first_name)
                form.addRow("Last Name:", self.last_name)
                form.addRow("Date of Birth (MM/DD/YYYY):", self.dob)
                form.addRow("Sex:", self.sex)

                self.layout.addLayout(form)
                
                self.buttons = QDialogButtonBox(
                        QDialogButtonBox.StandardButton.Cancel
                        | QDialogButtonBox.StandardButton.Ok
                )
                self.buttons.accepted.connect(self.save_patient)
                self.buttons.rejected.connect(self.reject)

                self.layout.addWidget(self.buttons)
                self.setLayout(self.layout)

        patient_added = pyqtSignal()

        def save_patient(self):
                try:
                        new_patient = PatientData(
                                mrn = self.mrn.text(),
                                first_name = self.first_name.text(),
                                last_name = self.last_name.text(),
                                dob = self.dob.text(),
                                sex = self.sex.text()
                        )
                        self.session.add(new_patient)
                        self.session.commit()
                        QMessageBox.information(self, "Success", "New Patient Added")

                        self.patient_added.emit()
                        self.accept()
                except Exception as e:
                        self.session.rollback()
                        QMessageBox.critical(self, "Error", f"Could not add new patient: {e}")

if __name__ == "__main__":
        app = QApplication([])
        add_patient = AddPatient()
        add_patient.show()
        sys.exit(app.exec())