'''
Author: David Porfirio
'''

class Category:

    '''
    Class: Category
    Purpose: Contains all of the data relevant to a particular chore category
        including:
        1) the icon associated with the category
        2) the chores included in the category
    '''

    def __init__(self, name, img_file):
        self.name = name
        self.img = img_file
        self.chores = []
