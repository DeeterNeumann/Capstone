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
    QTabWidget
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

        self.tab_widget.addTab(PatientIdTab(), "Patient Data")
        self.tab_widget.addTab(DiagnosisTab(), "Diagnosis")
        self.tab_widget.addTab(CARProductTab(), "Product Info")
        self.tab_widget.addTab(TherapyDetailsTab(), "Therapy Details")
        self.tab_widget.addTab(SideEffectsTab(), "Side Effects")
        self.tab_widget.addTab(LabValuesTab(), "Lab Values")
        self.tab_widget.addTab(OutcomesTab(), "Outcomes")

    def _createDisplay(self):
        self.display = QTableView()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        # self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        # self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def _createMenu(self):
        menu = self.menuBar().addMenu("&Menu")
        menu.addAction("&Exit", self.close)

    # def _createToolBar(self):
    #     tools = QToolBar()
    #     tools.addAction("Exit", self.close)
    #     self.addToolBar(tools)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("Status Bar")
        self.setStatusBar(status)

def main():
    """PyCARToxDB's main function."""
    pycarApp = QApplication([])
    pycarWindow = PyCARToxDBWindow()
    pycarWindow.show()
    sys.exit(pycarApp.exec())
    
if __name__ == "__main__":
    # app = QApplication([])
    # window = PyCARToxDBWindow()
    # window.show()
    main()
    # sys.exit(app.exec())



# Set cells to read only
# Create state in page - everything disabled unless clicking edit button

# SQL server may not be the best
# SQLite - local file base