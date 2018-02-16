#!/usr/bin/env python3

"""
A small database program to illustrate one approach.  From:
https://www.reddit.com/r/learnpython/comments/7xvwlt/help_with_user_input_data_storage/
"""

import sys
import json
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from PyQt5.QtWidgets import QPushButton, QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QHBoxLayout
from PyQt5.QtCore import Qt


# name and version number of the template
ExName = '"Database" example'
ExVersion = '0.1'

# width and height of top-level widget
WidgetWidth = 600
WidgetHeight = 150

###########################################
# The "database" code - just a set of functions.
# This could be a class, and/or in a different module.
###########################################

def read_database(filename):
    """Prepare the database given the data filename.
    
    Returns a "database object".
    """

    try:
        with open(filename, 'r') as fp:
            data = json.load(fp)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print(f'Database file "{filename}" not found or corrupt')
        data = {}       # no data, initialize the "database"

    return data

def save_database(db, filename):
    with open(filename, 'w') as fp:
        json.dump(db, fp, sort_keys=True, indent=2)

def get_student(database, name):
    """Given a student 'name', return student data as a dict,i
    or None if not found."""

    return database.get(name, None)

def put_student(database, name, age, height):
    """Save student record in the in-memory database."""

    database[name] = {'age': age, 'height': height}

###########################################
# The "GUI" code.
###########################################

DatabaseFilename = 'data.db'

class Template(QWidget):

    def __init__(self):
        super().__init__()
        self.database = read_database(DatabaseFilename)
        self.initUI()

        # miscellaneous stuff
        self.setGeometry(300, 300, WidgetWidth, WidgetHeight)
        self.setWindowTitle('%s %s' % (ExName, ExVersion))
        self.show()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        # row 0 of grid
        label = QLabel('Name:')
        label.setAlignment(Qt.AlignRight)
        grid.addWidget(label, 0, 0)

        self.qle_name = QLineEdit(self)
        grid.addWidget(self.qle_name, 0, 1)

        label = QLabel('    ')      # add a little spacer
        grid.addWidget(label, 0, 2)

        label = QLabel('Age:')
        label.setAlignment(Qt.AlignRight)
        grid.addWidget(label, 0, 3)

        self.qle_age = QLineEdit(self)
        grid.addWidget(self.qle_age, 0, 4)

        # row 1 of grid
        label = QLabel('Height:')
        label.setAlignment(Qt.AlignRight)
        grid.addWidget(label, 1, 3)

        self.qle_height = QLineEdit(self)
        grid.addWidget(self.qle_height, 1, 4)

        # row 2 - could use some vertical separation - just put empty label
        label = QLabel('')
        grid.addWidget(label, 2, 4)

        # row 3 of grid - a horizontal box containing buttons
        hbox = QHBoxLayout()

        hbox.addStretch(1)

        btn = QPushButton('Load', self)
        btn.clicked.connect(self.loadUser)
        hbox.addWidget(btn)

        btn = QPushButton('Clear', self)
        hbox.addWidget(btn)
        btn.clicked.connect(self.clearFields)

        btn = QPushButton('Save', self)
        hbox.addWidget(btn)
        btn.clicked.connect(self.saveUser)

        grid.addLayout(hbox, 3, 4, 4, 1)

    def clearFields(self):
        """Clear all GUI fields."""

        self.qle_name.clear()
        self.qle_age.clear()
        self.qle_height.clear()

    def loadUser(self):
        """Get data for a user from database.

        Uses the "name" lineedit to query the database
        and populate the other fields.
        """

        name = self.qle_name.text()
        if not name:
            msg = f"Sorry, you must supply a name"
            QMessageBox.warning(self, "Problem", msg)
            return

        student = get_student(self.database, name)
        if not student:
            msg = f"Sorry, student '{name}' doesn't exist in the database"
            QMessageBox.warning(self, "Problem", msg)
        else:
            age = student.get('age', '')
            height = student.get('height', '')
            self.qle_age.setText(str(age))
            self.qle_height.setText(str(height))

    def saveUser(self):
        """Save student data in lineedits to the in-memory structure."""

        name = self.qle_name.text()
        if not name:
            msg = f"Sorry, you can't save a student without a name."
            QMessageBox.warning(self, "Problem", msg)
        else:
            age = self.qle_age.text()
            age = f'{float(age):.1f}'
            height = self.qle_height.text()
            height = f'{float(height):.1f}'
            put_student(self.database, name, age, height)

    def closeEvent(self, event):
        save_database(self.database, DatabaseFilename)
        event.accept()


app = QApplication([])
ex = Template()
sys.exit(app.exec_())
