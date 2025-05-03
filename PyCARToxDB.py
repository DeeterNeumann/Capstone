import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
)

from PyCARToxDBWindow_class import PyCARToxDBWindow

def main(self):
    """PyCARToxDB's main function."""
    pycarApp = QApplication([])
    pycarWindow = PyCARToxDBWindow()
    pycarWindow.show()
    PyCARToxDB(model = *****, view=pycarWindow)
    sys.exit(pycarApp.exec())


    """PyCARToxDB's main function."""
    pycarApp = QApplication([])
    pycarWindow = PyCalcWindow()
    pycarWindow.show()
    PyCalc(model=evaluateExpression, view=pycarWindow)
    sys.exit(pycarApp.exec())



# user entry
# validate (ensure everything is appropriate)
# save to database
# read from database
# populate fields from database
# # Business logic is reading and writing from the database
# # The model code reads and writes to the database
# # Send the data from the database to the controller
# # Controller using the model to access the database and will populate in the view