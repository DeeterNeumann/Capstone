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
from model.lab_values_model import LabValues

Session = sessionmaker(bind=engine)

class AddLabValues(QDialog):
    def __init__(self, parent=None):
            super().__init__(parent)
            self.setWindowTitle("Add Lab Values")
            self.session = Session()

            self.layout = QVBoxLayout()
            form = QFormLayout()
                
            self.patient_id = QLineEdit()
            self.date = QLineEdit()
            self.CRP = QLineEdit()
            self.ferritin = QLineEdit()
            self.IL6 = QLineEdit()
            self.WBC = QLineEdit()
            self.Hgb = QLineEdit()
            self.Plt = QLineEdit()
            self.ANC = QLineEdit()
            self.ALC = QLineEdit()
            self.AST = QLineEdit()
            self.ALT = QLineEdit()
            self.tBili = QLineEdit()
            self.BUN = QLineEdit()
            self.sCr = QLineEdit()
            self.PT = QLineEdit()
            self.INR = QLineEdit()
            self.Ddimer = QLineEdit()
            self.fibrinogen = QLineEdit()

            form.addRow("Patient ID:", self.patient_id)
            form.addRow("Date:", self.date)
            form.addRow("CRP:", self.CRP)
            form.addRow("Ferritin:", self.ferritin)
            form.addRow("IL6:", self.IL6)
            form.addRow("WBC:", self.WBC)
            form.addRow("Hgb:", self.Hgb)
            form.addRow("Plt:", self.Plt)
            form.addRow("ANC:", self.ANC)
            form.addRow("ALC:", self.ALC)
            form.addRow("AST:", self.AST)
            form.addRow("ALT:", self.ALT)
            form.addRow("tBili:", self.tBili)
            form.addRow("BUN", self.BUN)
            form.addRow("sCr:", self.sCr)
            form.addRow("PT:", self.PT)
            form.addRow("INR:", self.INR)
            form.addRow("Ddimer:", self.Ddimer)
            form.addRow("Fibrinogen;", self.fibrinogen)

            self.layout.addLayout(form)
                
            self.buttons = QDialogButtonBox(
                    QDialogButtonBox.StandardButton.Cancel
                    | QDialogButtonBox.StandardButton.Ok
                )
            self.buttons.accepted.connect(self.save_lab_values)
            self.buttons.rejected.connect(self.reject)

            self.layout.addWidget(self.buttons)
            self.setLayout(self.layout)

    lab_values_added = pyqtSignal()

    def save_lab_values(self):
        try:
            new_lab_values = LabValues(
                patient_id = self.patient_id.text(),
                date = self.date.text(),
                CRP = self.CRP.text(),
                ferritin = self.ferritin.text(),
                IL6 = self.IL6.text(),
                WBC = self.WBC.text(),
                Hgb = self.Hgb.text(),
                Plt = self.Plt.text(),
                ANC = self.ANC.text(),
                ALC = self.ALC.text(),
                AST = self.AST.text(),
                ALT = self.ALT.text(),
                tBili = self.tBili.text(),
                BUN = self.BUN.text(),
                sCr = self.sCr.text(),
                PT = self.PT.text(),
                INR = self.INR.text(),
                Ddimer = self.Ddimer.text(),
                fibrinogen = self.fibrinogen.text()
            )
            
            self.session.add(new_lab_values)
            self.session.commit()
            QMessageBox.information(self, "Success", "Lab Values Added")

            self.lab_values_added.emit()
            self.accept()
        except Exception as e:
            self.session.rollback()
            QMessageBox.critical(self, "Error", f"Could not lab values: {e}")

if __name__ == "__main__":
        app = QApplication([])
        add_lab_values = AddLabValues()
        add_lab_values.show()
        sys.exit(app.exec())