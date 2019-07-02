'''
Author: David Porfirio
'''

from PyQt5.QtWidgets import QLabel, QPushButton

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
                button = QPushButton(chore, parent=self)
                button.move(100*j,100*i)
                button.setFixedSize(100,100)
                chore_counter += 1
                if chore_counter >= len(chore_list):
                    break
            if chore_counter >= len(chore_list):
                break
