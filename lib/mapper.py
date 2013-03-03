from os import sep, listdir, path
from lib.image import Image
from lib.matcher import Matcher


class Mapper():

    def __init__(self):
        self._matchers = self._create_matchers()
        self._buttons = {}

        self._create_button_mappings()

    def _create_matchers(self):
        matchers = []

        for path in self._get_image_paths():
            image = Image(path)
            matcher = Matcher(image)
            matchers.append(matcher)

        return matchers

    def _get_image_paths(self):
        abs_image_dir = self._resolve_root_image_dir()
        file_paths = []

        for file in listdir(abs_image_dir):
            file_paths.append(abs_image_dir + sep + file)

        return file_paths

    def _resolve_root_image_dir(self):
        relative_image_dir = 'images' + sep + 'buttons'
        return path.abspath(relative_image_dir)

    def _create_button_mappings(self):
        for matcher in self._matchers:
            self._buttons[matcher.get_action()] = matcher.get_coordinates()

    def get(self, key):
        return self._buttons[key]
