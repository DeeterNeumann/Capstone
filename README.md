# Capstone

## Description

PyCARToxDB is a graphical user interface (GUI) connected to a SQLite database that allows for the collection of information relevant to a patient's chimeric antigen receptor (CAR) T cell therapy, which individual tabs for the following:

- Patient Information
- Diagnosis
- Past Cancer Treatment History
- CAR T Product
- CAR T Treatment Details
- Side Effects and Management
- Lab Values
- Treatment Outcomes

Patient data can be added in each tab via the respective option found in the GUI Menu.

Currently, data on the patient information tab can be edited and deleted via the buttons on the tool bar. Currently, data in all other tabs can be edited via clicking individual cells in the spreadsheet with future plans to add buttons for each tab.

Of note, the file "test_main.py" is used to test various functionalities and relationships outside of the main window.

## Steps for Running

After cloning from GitHub and activating a virtual environment (suggested) the program can be run by entering the following in the terminal:

1. pip install -r requirements.txt
2. python3 .\PyCARToxWindow_class.py