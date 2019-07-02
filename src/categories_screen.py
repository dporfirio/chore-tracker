'''
Author: David Porfirio
'''

from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QButtonGroup

class CategoriesScreen(QWidget):

    '''
    Class: CategoriesScreen
    Purpose: Contains the category buttons
    '''

    def __init__(self, categories, parent):
        super(CategoriesScreen, self).__init__(parent=parent)

        self.setGeometry(0,0,700,100)
        layout = QHBoxLayout()
        layout.setSpacing(0)

        self.buttons = QButtonGroup()
        self.buttons.setExclusive(True)
        for cat in categories:
            button = QPushButton(cat)
            button.setFixedSize(700*1.0/len(categories), 100)
            self.buttons.addButton(button)
            button.setCheckable(True)
            layout.addWidget(button)

        self.buttons.buttonClicked.connect(parent.display_chores)

        self.setLayout(layout)
        button.setChecked(True)
        self.curr_active = button
