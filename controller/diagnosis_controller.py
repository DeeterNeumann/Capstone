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
from model.diagnosis_model import Diagnosis

Session = sessionmaker(bind=engine)

class AddDiagnosis(QDialog):
        def __init__(self, parent=None):
                super().__init__(parent)
                self.setWindowTitle("Add Diagnosis")
                self.session = Session()

                self.layout = QVBoxLayout()
                form = QFormLayout()
                
                self.patient_id = QLineEdit()
                self.diagnosis_name = QLineEdit()

                form.addRow("Patient ID:", self.patient_id)
                form.addRow("Diagnosis:", self.diagnosis_name)

                self.layout.addLayout(form)
                
                self.buttons = QDialogButtonBox(
                        QDialogButtonBox.StandardButton.Cancel
                        | QDialogButtonBox.StandardButton.Ok
                )
                self.buttons.accepted.connect(self.save_diagnosis)
                self.buttons.rejected.connect(self.reject)

                self.layout.addWidget(self.buttons)
                self.setLayout(self.layout)

        diagnosis_added = pyqtSignal()

        def save_diagnosis(self):
                try:
                        new_diagnosis = Diagnosis(
                                patient_id = self.patient_id.text(),
                                diagnosis_name = self.diagnosis_name.text(),
                        )
                        self.session.add(new_diagnosis)
                        self.session.commit()
                        QMessageBox.information(self, "Success", "Diagnosis Added")

                        self.diagnosis_added.emit()
                        self.accept()
                except Exception as e:
                        self.session.rollback()
                        QMessageBox.critical(self, "Error", f"Could not add new diagnosis: {e}")

if __name__ == "__main__":
        app = QApplication([])
        add_diagnosis = AddDiagnosis()
        add_diagnosis.show()
        sys.exit(app.exec())