

# model-view-controller design pattern
# # Model
# # # handles app's business logic
# # # contains core functionality and data
# # View
# # # implements app's GUI
# # # hosts all widgets (to allow interaction with application)
# # # receives user's actions and events
# # Controller
# # # connects the Model and the View
# # # events sent to Controller
# # # puts model to work
# # # Controller forwards Model response to 

# Calculator Application
# # User performs an action
# # the View notifies the Controller
# # the Controller gets the User's request and queries the Model
# # the Model processes the Query and returns the Result
# # the Controller receives the Response and updates the View
# # the User sees the requested Result on the View

# Creating your calculator app
# # Implement minimal application skeleton
# # Create pycalc.py
# # Completed file available in Course Materials


# The Model
# # Calculator App


### Review documentations
# PySide
# 

# user entry
# validate (ensure everything is appropriate)
# save to database
# read from database
# populate fields from database
# # Business logic is reading and writing from the database
# # The model code reads and writes to the database
# # Send the data from the database to the controller
# # Controller using the model to access the database and will populate in the view