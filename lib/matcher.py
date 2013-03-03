from cv2 import matchTemplate, TM_CCOEFF
import numpy as np
from lib.image import Image


class Matcher():
    # @ToDo: TEMPLATE should be a screen grab - np.asarray(ImageGrab.grab())[:,:,::-1].copy()
    TEMPLATE = Image('C:\\dev\\python\\rbot\\images\\template.bmp').mat
    OFFSET = 15

    def __init__(self, image, match_method=''):
        self._button = image
        self._match_result = self._find_button()

    def _find_button(self):
        return matchTemplate(self._button.mat, Matcher.TEMPLATE, TM_CCOEFF)

    def _get_raw_coordinates(self):
        return np.unravel_index(self._match_result.argmax(), self._match_result.shape)

    def _adjust_coordinates(self, numpy_coords):
        x = int(numpy_coords[1])
        y = int(numpy_coords[0])

        return (x+Matcher.OFFSET, y+Matcher.OFFSET)

    def get_coordinates(self):
        return self._adjust_coordinates(self._get_raw_coordinates())

    def get_action(self):
        return self._button.name
