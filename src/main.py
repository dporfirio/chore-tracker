'''
Author: David Porfirio
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
from main_display import *
from tracker import *

class App(QMainWindow):

    '''
    Class: App
    Purpose: Contains the highest level window components, and maintains
        the window.
    '''

    def __init__(self):
        super(App, self).__init__()
        self.title = 'Chore Tracker'
        self.width, self.height = 800,480
        data_filename = sys.argv[1]
        self.tracker = Tracker(data_filename)
        self.init_ui()
        self.show()

    def init_ui(self):

        '''
        Method: init_ui
        Purpose: Initialize components within the main window
        '''
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, self.width, self.height)
        main_display = MainDisplay(self.tracker, self)

if __name__ == "__main__":

    # start the GUI
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
