from cv2 import imread 
from os import sep


class Image():

    def __init__(self, path):
        self.path = path
        self.name = self._resolve_image_name()
        self.mat = self._create_image_mat()

    def _resolve_image_name(self):
        split_path = self.path.split(sep)
        image_name_with_extension = split_path[len(split_path)-1]

        return image_name_with_extension.split('.')[0]

    def _create_image_mat(self):
        return imread(self.path)
