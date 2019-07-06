'''
Author: David Porfirio
'''

class Chore:

    '''
    Class: Chore
    Purpose: Contains all of the data relevant to a particular chore including:
        1) the icon associated with the chore
    '''

    def __init__(self, name, img_file):
        self.name = name
        self.img = img_file
