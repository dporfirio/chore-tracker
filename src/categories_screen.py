'''
Author: David Porfirio
'''

from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QButtonGroup
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize, Qt

class CategoriesScreen(QWidget):

	'''
	Class: CategoriesScreen
	Purpose: Contains the category buttons
	'''

	def __init__(self, categories, parent):
		super(CategoriesScreen, self).__init__(parent=parent)

		self.setGeometry(0,0,800,100)
		layout = QHBoxLayout()
		layout.setSpacing(0)

		self.buttons = QButtonGroup()
		self.buttons.setExclusive(True)
		self.button2category = {}
		for cat in categories:
			button = QPushButton()
			button.setFixedSize(800*1.0/len(categories)-4, 100)
			button.setStyleSheet("QPushButton { background-color: white }")
			icon  = QIcon("img/{}".format(cat.img))
			button.setIcon(icon);
			button.setIconSize(QSize(30,30))
			self.button2category[button] = cat
			self.buttons.addButton(button)
			button.setCheckable(True)
			layout.addWidget(button)

		self.buttons.buttonClicked.connect(parent.display_chores)

		self.setLayout(layout)
		button.setChecked(True)
		self.curr_active = button
