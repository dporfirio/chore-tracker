'''
Author: David Porfirio
'''

import csv
from chore import *

class Reader:

    '''
    Class: Reader
    Purpose: Reads and saves the chore data to CSV files
    '''

    def __init__(self):
        pass

    def read(self, filename):

        '''
        Method: read
        Purpose: Read the chore data from a CSV file
        '''

        chores = {}
        with open(filename, "r") as infile:
            csv_reader = csv.reader(infile, delimiter=',')
            rowcount = 0
            for row in csv_reader:
                if rowcount > 0:
                    row_cat = row[1]
                    row_chore = Chore(row[0], row[2])

                    if row_cat not in chores:
                        chores[row_cat] = []
                    chores[row_cat].append(row_chore)

                rowcount += 1
        return chores
