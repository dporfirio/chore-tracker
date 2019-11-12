'''
Author: David Porfirio
'''

import csv
from chore import *
from category import *

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

		categories = {}
		with open(filename, "r") as infile:
			csv_reader = csv.reader(infile, delimiter=',')
			rowcount = 0
			for row in csv_reader:
				if rowcount > 0:
					row_cat = row[1]
					row_chore = Chore(row[0], row[2])

					if row_cat not in categories:
						categories[row_cat] = Category(row_cat,row[3])
					categories[row_cat].chores.append(row_chore)

				rowcount += 1
		return categories
