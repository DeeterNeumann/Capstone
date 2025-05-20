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

from controller.patient_controller import AddPatient

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
        self.diagnosis = DiagnosisTab()
        self.car_product = CARProductTab()
        self.therapy = TherapyDetailsTab()
        self.side_effects = SideEffectsTab()
        self.labs = LabValuesTab()
        self.outcomes = OutcomesTab()

        self.tab_widget.addTab(self.patient_id, "Patient Data")
        self.tab_widget.addTab(self.diagnosis, "Diagnosis")
        self.tab_widget.addTab(self.car_product, "Product Info")
        self.tab_widget.addTab(self.therapy, "Therapy Details")
        self.tab_widget.addTab(self.side_effects, "Side Effects")
        self.tab_widget.addTab(self.labs, "Lab Values")
        self.tab_widget.addTab(self.outcomes, "Outcomes")

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

def main():
    """PyCARToxDB's main function."""
    pycarApp = QApplication([])
    pycarWindow = PyCARToxDBWindow()
    pycarWindow.show()
    sys.exit(pycarApp.exec())
    
if __name__ == "__main__":
    main()