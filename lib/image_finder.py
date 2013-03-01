import cv2
import numpy as np
from PIL import Image, ImageGrab

class ImageFinder():

	def __init__(self):
		# self.template = self.set_template()
		self.template = cv2.imread('C:\\dev\\python\\rbot\\images\\template.bmp')
		self.button = None
		self.match_result = None

	def set_template(self):
		self.template = np.asarray(ImageGrab.grab())[:,:,::-1].copy()

	def set_button(self, image_path):
		self.button = cv2.imread(image_path)

	def find_button(self, image_path):
		self.set_button(image_path)
		self.match_result = cv2.matchTemplate(self.button, self.template, cv2.TM_CCOEFF)

	def get_coordinates(self):
		return np.unravel_index(self.match_result.argmax(), self.match_result.shape)