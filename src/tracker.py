'''
Author: David Porfirio
'''

from reader import *

class Tracker:

    '''
    Class: ChoreScreen
    Purpose: Contains and updates the chore data. Also controls access to the
        chore data.
    '''

    def __init__(self, filename):
        reader = Reader()
        self.data = reader.read(filename)
