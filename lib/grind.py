from autopy import *
from time import sleep

class Grind():

	def __init__(self, button_map):
		self.button_map = button_map
		print self.button_map
		self.grind()

	def grind(self):
		while(True):
			self.click_button("target")
			self.click_button("attack")
			print "sleeping..."
			sleep(8)
			print "done sleeping"
			self.click_button("pickup")
			sleep(2)

	def click_button(self, button):
		print "clicking ", button
		coord_tuple = self.button_map[button]
		mouse.move(coord_tuple[0], coord_tuple[1])
		mouse.click()
		mouse.click()
