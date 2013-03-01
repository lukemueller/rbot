from lib import image_finder
import os

class CoordinateMapper():

	def __init__(root_image_dir):
		self.root_image_dir = root_image_dir
		self.buttons = self.get_buttons()
		self.button_coords = {}
		self.image_finder = image_finder.ImageFinder()
		self.offset = 10
  	
	def get_buttons(self):
		button_list
		for root, dir, files in os.walk(self.root_image_dir):
			button_list = files

		return button_list

	def map_buttons(self):
		for button_name in self.buttons:
			self.image_finder.find_button(self.root_image_dir + os.sep + button_name)
			coords = self.image_finder.get_coordinates()
			self.button_coords[self.drop_extension(button_name)] = self.coords_as_xy_tuple(coords)

	def drop_extension(self, image_name):
		return image_name.split('.')[0]

	def coords_as_xy_tuple(self, numpy_coords):
		return (int(numpy_coords[1]), int(numpy_coords[0]))