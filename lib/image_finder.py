import cv2
import numpy as np
from PIL import ImageGrab

class ImageFinder():

	def __init__():
		self.template = self.set_template()
		self.button
		self.match_result

	def set_template(self):
		self.template = np.asarray(ImageGrab.grab().getdata())

	def get_mat(self, image_path):
		return cv2.imread(image_path)

	def find_button(self, image_path):
		self.match_result = cv2.matchTemplate(self.get_mat(image_path), self.template, cv2.TM_CCOEFF)

	def get_coordinates(self):
		return np.unravel_index(self.match_result.argmax(), self.match_result.shape)