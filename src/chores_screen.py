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

    def __init__(self, chore_list, parent):
        super(ChoreScreen, self).__init__(parent=parent)
        self.chore_list = chore_list

        self.setGeometry(0, 120, 700, 200)

        chore_counter = 0
        for i in range(3):
            for j in range(7):
                chore = chore_list[chore_counter]
                button = QPushButton("", parent=self)
                button.move(100*j,100*i)
                button.setFixedSize(100,100)
                button.setStyleSheet("QPushButton { background-color: white }")
                icon  = QIcon("img/{}".format(chore.img))
                button.setIcon(icon);
                button.setIconSize(QSize(30,30))
                chore_counter += 1
                if chore_counter >= len(chore_list):
                    break
            if chore_counter >= len(chore_list):
                break
