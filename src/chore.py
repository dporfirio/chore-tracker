'''
Author: David Porfirio
'''

import datetime

class Chore:

    '''
    Class: Chore
    Purpose: Contains all of the data relevant to a particular chore including:
        1) the icon associated with the chore
    '''

    def __init__(self, name, img_file):
        self.name = name
        self.img = img_file
        self.datetime = datetime.datetime.now()
        self.UI_callback = None

    def update(self):

         if self.UI_callback is not None:
             self.UI_callback(1)

    def set_UI_callback(self, func):
        self.UI_callback = func
