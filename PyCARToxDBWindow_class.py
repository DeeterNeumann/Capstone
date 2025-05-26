from PyCARToxDB_constants import (
    WINDOWSIZE_WIDTH, 
    WINDOWSIZE_HEIGHT, 
    DISPLAY_WIDTH, 
    DISPLAY_HEIGHT
)

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QTableView,
    QWidget,
    QStatusBar,
    # QToolBar,
    QTabWidget,
    QDialog
)
from PyQt6.QtGui import (
    QStandardItemModel,
    QStandardItem
)

from tab.patient_id import PatientIdTab
from tab.diagnosis import DiagnosisTab
from tab.car_product import CARProductTab
from tab.therapy_details import TherapyDetailsTab
from tab.side_effects import SideEffectsTab
from tab.lab_values import LabValuesTab
from tab.outcomes import OutcomesTab
from tab.tx_history import TxHistoryTab

from controller.patient_controller import AddPatient
from controller.diagnosis_controller import AddDiagnosis
from controller.car_product_controller import AddCARProduct
from controller.therapy_controller import AddTherapyDetails
from controller.side_effect_controller import AddSideEffect
from controller.lab_values_controller import AddLabValues
from controller.outcomes_controller import AddOutcome
from controller.tx_history_controller import AddTreatmentHistory

class PyCARToxDBWindow(QMainWindow):
    """PyCARToxDB's main window."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyCARToxDB")
        self.setFixedSize(WINDOWSIZE_WIDTH, WINDOWSIZE_HEIGHT)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self._createDisplay()
        self._createMenu()
        # self._createToolBar()
        self._createStatusBar()

        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        self.patient_id = PatientIdTab(status_bar=self.status)
        self.diagnosis = DiagnosisTab(status_bar=self.status)
        self.car_product = CARProductTab(status_bar=self.status)
        self.therapy_details = TherapyDetailsTab(status_bar=self.status)
        self.side_effects = SideEffectsTab(status_bar=self.status)
        self.labs = LabValuesTab(status_bar=self.status)
        self.outcomes = OutcomesTab(status_bar=self.status)
        self.tx_history = TxHistoryTab(status_bar=self.status)

        self.tab_widget.addTab(self.patient_id, "Patient Data")
        self.tab_widget.addTab(self.diagnosis, "Diagnosis")
        self.tab_widget.addTab(self.car_product, "Product Info")
        self.tab_widget.addTab(self.therapy_details, "Therapy Details")
        self.tab_widget.addTab(self.side_effects, "Side Effects")
        self.tab_widget.addTab(self.labs, "Lab Values")
        self.tab_widget.addTab(self.outcomes, "Outcomes")
        self.tab_widget.addTab(self.tx_history, "Treatment History")

    def _createDisplay(self):
        self.display = QTableView()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        # self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        # self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def _createMenu(self):
        menu = self.menuBar().addMenu("&Menu")
        menu.addAction("&Exit", self.close)
        menu.addAction("&Add Patient", self.open_add_patient_dialog)
        menu.addAction("&Add Diagnosis", self.open_add_diagnosis_dialog)
        menu.addAction("&Add CAR Product", self.open_add_product_dialog)
        menu.addAction("&Add Therapy Details", self.open_add_therapy_details_dialog)
        menu.addAction("&Add Side Effect", self.open_add_side_effect_dialog)
        menu.addAction("&Add Lab Values", self.open_add_lab_values_dialog)
        menu.addAction("&Add Outcome", self.open_add_outcome_dialog)
        menu.addAction("&Add Treatment History", self.open_add_treatment_history_dialog)

    # def _createToolBar(self):
    #     tools = QToolBar()
    #     tools.addAction("Exit", self.close)
    #     self.addToolBar(tools)

    def _createStatusBar(self):
        self.status = QStatusBar()
        self.status.showMessage("Status Bar")
        self.setStatusBar(self.status)

    def open_add_patient_dialog(self):
        dialog = AddPatient()
        dialog.patient_added.connect(self.patient_id.refresh_model)
        dialog.exec()

    def open_add_diagnosis_dialog(self):
        dialog = AddDiagnosis()
        dialog.diagnosis_added.connect(self.diagnosis.refresh_model)
        dialog.exec()

    def open_add_product_dialog(self):
        dialog = AddCARProduct()
        dialog.product_added.connect(self.car_product.refresh_model)
        dialog.exec()

    def open_add_therapy_details_dialog(self):
        dialog = AddTherapyDetails()
        dialog.therapy_details_added.connect(self.therapy_details.refresh_model)
        dialog.exec()
    
    def open_add_side_effect_dialog(self):
        dialog = AddSideEffect()
        dialog.side_effect_added.connect(self.side_effects.refresh_model)
        dialog.exec()
    
    def open_add_lab_values_dialog(self):
        dialog = AddLabValues()
        dialog.lab_values_added.connect(self.labs.refresh_model)
        dialog.exec()

    def open_add_outcome_dialog(self):
        dialog = AddOutcome()
        dialog.outcome_added.connect(self.outcomes.refresh_model)
        dialog.exec()

    def open_add_treatment_history_dialog(self):
        dialog = AddTreatmentHistory()
        dialog.treatment_history_added.connect(self.tx_history.refresh_model)
        dialog.exec()

def main():
    """PyCARToxDB's main function."""
    pycarApp = QApplication([])
    pycarWindow = PyCARToxDBWindow()
    pycarWindow.show()
    sys.exit(pycarApp.exec())
    
if __name__ == "__main__":
    main()