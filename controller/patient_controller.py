import sys

from datetime import date

from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QInputDialog,
    QLineEdit,
    QVBoxLayout,
    QPushButton,
    QMessageBox,
    QDateEdit
)

from PyQt6.QtCore import pyqtSignal, QDate
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
                self.dob = QDateEdit(calendarPopup=True)
                self.bio_sex = QLineEdit()

                form.addRow("MRN:", self.mrn)
                form.addRow("First Name:", self.first_name)
                form.addRow("Last Name:", self.last_name)
                form.addRow("Date of Birth (MM/DD/YYYY):", self.dob)
                form.addRow("Biological Sex:", self.bio_sex)

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
                        qdate = self.dob.date()
                        py_date = date(qdate.year(), qdate.month(), qdate.day())
                        new_patient = PatientData(
                                mrn = self.mrn.text(),
                                first_name = self.first_name.text(),
                                last_name = self.last_name.text(),
                                dob = py_date,
                                bio_sex = self.bio_sex.text()
                        )
                        self.session.add(new_patient)
                        self.session.commit()
                        QMessageBox.information(self, "Success", "New Patient Added")

                        self.patient_added.emit()
                        self.accept()
                except Exception as e:
                        self.session.rollback()
                        QMessageBox.critical(self, "Error", f"Could not add new patient: {e}")

class EditPatient(QDialog):

        def __init__(self, row_instance, Session, parent=None):
                super().__init__(parent)
                self.row = row_instance
                self.setWindowTitle("Edit Patient")
                self.session = Session
                py_date = self.row.dob

                self.layout = QVBoxLayout()

                self.mrn_edit = QLineEdit(self.row.mrn)
                self.first_name_edit = QLineEdit(self.row.first_name)
                self.last_name_edit = QLineEdit(self.row.last_name)
                self.dob_edit = QDateEdit(calendarPopup = True)
                self.dob_edit.setDate(QDate(py_date.year, py_date.month, py_date.day))
                self.bio_sex_edit = QLineEdit(self.row.bio_sex)

                self.save_button = QPushButton("Save")
                self.save_button.clicked.connect(self.save_changes)

                self.layout.addWidget(self.mrn_edit)
                self.layout.addWidget(self.first_name_edit)
                self.layout.addWidget(self.last_name_edit)
                self.layout.addWidget(self.dob_edit)
                self.layout.addWidget(self.bio_sex_edit)
                self.layout.addWidget(self.save_button)

                self.setLayout(self.layout)
        
        patient_edited = pyqtSignal()

        def save_changes(self):
                self.row.mrn = self.mrn_edit.text()
                self.row.first_name = self.first_name_edit.text()
                self.row.last_name = self.last_name_edit.text()
                qdate = self.dob_edit.date()
                self.row.dob = date(qdate.year(), qdate.month(), qdate.day())
                self.row.bio_sex = self.bio_sex_edit.text()

                with Session() as session:
                        self.session.merge(self.row)
                        self.session.commit()
                self.patient_edited.emit()
        
                self.accept()

if __name__ == "__main__":
        app = QApplication([])
        add_patient = AddPatient()
        add_patient.show()
        edit_patient = EditPatient()
        edit_patient.show()
        sys.exit(app.exec())