'''
Author: David Porfirio
'''

from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize

class ChoreScreen(QLabel):

    '''
    Class: ChoreScreen
    Purpose: Contains the chore buttons
    '''

    def __init__(self, category, parent):
        super(ChoreScreen, self).__init__(parent=parent)
        self.chore_list = category.chores

        self.setGeometry(0, 120, 700, 200)

        chore_counter = 0
        for i in range(3):
            for j in range(7):
                chore = self.chore_list[chore_counter]
                button = ChoreButton(parent=self)
                button.move(100*j,100*i)
                button.setFixedSize(100,100)
                button.setStyleSheet("QPushButton { background-color: white }")
                icon  = QIcon("img/{}".format(chore.img))
                button.setIcon(icon);
                button.setIconSize(QSize(30,30))
                chore.set_UI_callback(button.update_shade)
                chore_counter += 1
                if chore_counter >= len(self.chore_list):
                    break
            if chore_counter >= len(self.chore_list):
                break

class ChoreButton(QPushButton):

    def __init__(self, parent):
        super(ChoreButton, self).__init__(parent=parent)

    def update_shade(self, ratio):
        self.setStyleSheet("QPushButton { background-color: red }")
