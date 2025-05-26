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
from model.side_effects_model import SideEffects

Session = sessionmaker(bind=engine)

class AddSideEffect(QDialog):
        def __init__(self, parent=None):
                super().__init__(parent)
                self.setWindowTitle("Add Side Effect")
                self.session = Session()

                self.layout = QVBoxLayout()
                form = QFormLayout()
                
                self.patient_id = QLineEdit()
                self.therapy_id = QLineEdit()
                self.side_effect_type = QLineEdit()
                self.grade = QLineEdit()
                self.onset_date = QLineEdit()
                self.resolution_date = QLineEdit()
                self.management = QLineEdit()


                form.addRow("Patient ID:", self.patient_id)
                form.addRow("Therapy ID:", self.therapy_id)
                form.addRow("Type of Side Effect:", self.side_effect_type)
                form.addRow("Side Effect Grade:", self.grade)
                form.addRow("Side Effect Onset Date:", self.onset_date)
                form.addRow("Side Effect Resolution Date:", self.resolution_date)
                form.addRow("Side Effect Management:", self.management)

                self.layout.addLayout(form)
                
                self.buttons = QDialogButtonBox(
                        QDialogButtonBox.StandardButton.Cancel
                        | QDialogButtonBox.StandardButton.Ok
                )
                self.buttons.accepted.connect(self.save_side_effect)
                self.buttons.rejected.connect(self.reject)

                self.layout.addWidget(self.buttons)
                self.setLayout(self.layout)

        side_effect_added = pyqtSignal()

        def save_side_effect(self):
                try:
                        new_side_effect = SideEffects(
                                patient_id = self.patient_id.text(),
                                therapy_id = self.therapy_id.text(),
                                side_effect_type = self.side_effect_type.text(),
                                grade = self.grade.text(),
                                onset_date = self.onset_date.text(),
                                resolution_date = self.resolution_date.text(),
                                management = self.management.text()

                        )
                        self.session.add(new_side_effect)
                        self.session.commit()
                        QMessageBox.information(self, "Success", "New Side Effect Added")

                        self.side_effect_added.emit()
                        self.accept()
                except Exception as e:
                        self.session.rollback()
                        QMessageBox.critical(self, "Error", f"Could not add new side effect: {e}")

if __name__ == "__main__":
        app = QApplication([])
        add_side_effect = AddSideEffect()
        add_side_effect.show()
        sys.exit(app.exec())