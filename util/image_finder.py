from os import listdir, path
from lib.image import Image
from cv2 import matchTemplate, TM_CCOEFF
import numpy as np
from PIL import ImageGrab


class ImageFinder():

    def __init__(self, config):
        self._config = config
        self._images = self._get_images()
        self._match_results = {}

    def _get_images(self):
        images = []

        for image_path in self._get_image_paths():
            image = Image(image_path)
            images.append(image)

        return images

    def _get_image_paths(self):
        file_paths = []

        self._get_images_in_path(
            path.abspath(
                path.join('images', self._config.role)),
            file_paths)

        self._get_images_in_path(
            path.abspath(
                path.join('images', 'common')),
            file_paths)

        return file_paths

    def _get_images_in_path(self, root, paths):
        for file in listdir(root):
            image_path = path.join(root, file)
            paths.append(image_path)

        return paths

    def _match_all_images(self):
        for image in self._images:
            match_result = self._match(image)
            self._match_results[image] = match_result

    def _match(self, image):
        # ToDo - need a threshold for false matches
        return matchTemplate(image.mat, self._template, TM_CCOEFF)

    def _get_template(self):
        return np.asarray(ImageGrab.grab())[:,:,::-1].copy()

    def initialize(self):
        self._template = self._get_template()
        self._match_all_images()

    def get_matched_images(self):
        return self._match_results.items()
