from cv2 import matchTemplate
import numpy as np
from lib import Image


class Matcher():
    # @ToDo: TEMPLATE should be a screen grab - np.asarray(ImageGrab.grab())[:,:,::-1].copy()
    TEMPLATE = Image('template')
    OFFSET = 15

    def __init__(self, image, match_method='TM_CCOEFF'):
        self._button = image
        self._match_method = self._import_match_method(match_method)
        self._match_result = self._find_button()

    def _import_match_method(self, match_method):
        module = "cv2.%s" % match_method
        return __import__(module)

    def _find_button(self):
        return matchTemplate(self._button.mat(), Matcher.TEMPLATE, self._match_method)

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
