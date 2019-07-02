'''
Author: David Porfirio
'''

from PyQt5.QtWidgets import QLabel, QPushButton, QHBoxLayout, QButtonGroup
from categories_screen import *
from chores_screen import *

class MainDisplay(QLabel):

    '''
    Class: MainDisplay
    Purpose: Contains the displays for the chore categories, and the chore
        screens themselves.
    '''

    def __init__(self, tracker, parent):
        super(MainDisplay, self).__init__(parent=parent)
        self.tracker = tracker
        chores = self.tracker.data
        categories = chores.keys()
        self.setGeometry(50, 20, 700, 400)
        self.cat_screen = CategoriesScreen(categories, self)
        self.initialize_chore_screens()
        self.display_chores(self.cat_screen.curr_active)

    def initialize_chore_screens(self):

        '''
        Method: initialize_chore_screens
        Purpose: Initializes each individual screen corresponding to a set of
            chores corresponding to a particular category
        '''

        self.chore_screens = {}
        for cat in self.tracker.data:
            self.chore_screens[cat] = ChoreScreen(self.tracker.data[cat], self)
            self.chore_screens[cat].hide()

    def display_chores(self, btn):

        '''
        Method: display_chores
        Purpose: Called when category buttons are pressed to change the chore
            screen currently being displayed
        '''

        self.chore_screens[self.cat_screen.curr_active.text()].hide()
        self.chore_screens[btn.text()].show()
        self.cat_screen.curr_active = btn
