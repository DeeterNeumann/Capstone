import sys
from functools import partial
from PyQt6.QtWidgets import (
    QApplication, 
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QFormLayout,
    QPushButton,
    QLineEdit,
    QDialog,
    QDialogButtonBox,
    QMainWindow,
    QStatusBar,
    QToolBar,
    QLabel, 
    QWidget,
)

# app = QApplication([])

# window = QWidget()

# first GUI

# empty list - not handling
# often pass sys.argv to constructor of QApplication if need to handle script accept arguments
# app = QApplication([])

#  window = QWidget()
# window.setWindowTitle("PyQt App")
# window.setGeometry(100, 100, 280, 80)
# helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
# helloMsg.move(60, 15)

# #paint request to show GUI
# window.show()

# # call to exit to cleanly exit python and release resources
# sys.exit(app.exec())

# QBoxLayout



# window.setWindowTitle("QHBoxLayout")

# layout = QHBoxLayout()
# layout.addWidget(QPushButton("Left"))
# layout.addWidget(QPushButton("Center"))
# layout.addWidget(QPushButton("Right"))

# window.setLayout(layout)
# window.show()

# sys.exit(app.exec())

# v_layout.py

# window.setWindowTitle("QVBoxLayout")

# layout = QVBoxLayout()
# layout.addWidget(QPushButton("Top"))
# layout.addWidget(QPushButton("Center"))
# layout.addWidget(QPushButton("Bottom"))

#q_gridlayout.py

# window.setWindowTitle("QGridLayout")

# layout = QGridLayout()
# layout.addWidget(QPushButton("Button (0, 0)"), 0, 0)
# layout.addWidget(QPushButton("Button (0, 1)"), 0, 1)
# layout.addWidget(QPushButton("Button (0, 2)"), 0, 2)
# layout.addWidget(QPushButton("Button (1, 0)"), 1, 0)
# layout.addWidget(QPushButton("Button (1, 1)"), 1, 1)
# layout.addWidget(QPushButton("Button (1, 2)"), 1, 2)
# layout.addWidget(QPushButton("Button (2, 0)"), 2, 0)
# layout.addWidget(QPushButton("Button (2, 1) + 2 Columns Span"), 2, 1, 1, 2)

#f_layout.py
# Arranges widgets in two column layout
# First column usually displays messages and labels
# Second column usually contains widget that allows input such as QLineEdit, QComboBox, and so on. 
# Allows user to enter or edit data regarding the information in the first column


# window.setWindowTitle("QFormLayout")

# layout = QFormLayout()

# layout.addRow("Name:", QLineEdit())
# layout.addRow("Age:", QLineEdit())
# layout.addRow("Job:", QLineEdit())
# layout.addRow("Hobbies:", QLineEdit())

# window.setLayout(formLayout)
# window.show()

# sys.exit(app.exec())

# dialog

# class Window(QDialog):
#     def __init__(self):
#         super().__init__(parent=None) # set to none as set to main window
#         self.setWindowTitle("QDialog")
#         dialogLayout = QVBoxLayout()
#         formLayout = QFormLayout()
#         formLayout.addRow("Name:", QLineEdit())
#         formLayout.addRow("Age:", QLineEdit())
#         formLayout.addRow("Job:", QLineEdit())
#         formLayout.addRow("Hobbies:", QLineEdit())
#         dialogLayout.addLayout(formLayout)
#         buttons = QDialogButtonBox()
#         buttons.setStandardButtons(
#             QDialogButtonBox.StandardButton.Cancel
#             | QDialogButtonBox.StandardButton.Ok
#         )
#         dialogLayout.addWidget(buttons)
#         self.setLayout(dialogLayout)

# # will only run if intended code is executed as a program rather than imported as a module
# if __name__ == "__main__":
#     app = QApplication([])
#     window = Window()
#     window.show()
#     sys.exit(app.exec())

# Ok and cancel buttons don't do anything
# connect actions to buttons later in the course

# main_window

# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__(parent=None)
#         self.setWindowTitle("QMainWindow")
#         self.setCentralWidget(QLabel("I'm the Central Widget!"))
#         self._createMenu()
#         self._createToolBar()
#         self._createStatusBar()

#     def _createMenu(self):
#         menu = self.menuBar().addMenu("&Menu")
#         menu.addAction("&Exit", self.close)

#     def _createToolBar(self):
#         tools = QToolBar()
#         tools.addAction("Exit", self.close)
#         self.addToolBar(tools)

#     def _createStatusBar(self):
#         status = QStatusBar()
#         status.showMessage("I'm the Status Bar")
#         self.setStatusBar(status)

# if __name__ == "__main__":
#     app = QApplication([])
#     window = Window()
#     window.show()
#     sys.exit(app.exec())

# signals_slots

def greet(name):
    if msgLabel.text():
        msgLabel.setText("")
    else:
        msgLabel.setText(f"Hello, {name}!")

app = QApplication([])

window = QWidget()
window.setWindowTitle("Signal and slots")

layout = QVBoxLayout()

button = QPushButton("Greet")
button.clicked.connect(partial(greet, "World"))

layout.addWidget(button)
msgLabel = QLabel("")
layout.addWidget(msgLabel)

window.setLayout(layout)
window.show()

sys.exit(app.exec())

## Lambda function can replace functools.partial
## signals and slots give life you PyQT Applications
## turn user events into concrete actions
## dive deeper into signals and slots via PyQt documentation