from os import sep, listdir, path
from lib.image import Image
from cv2 import matchTemplate, TM_CCOEFF


# @ToDo: mapper should only map buttons for the user's role
class ImageFinder():
    # @ToDo: TEMPLATE should be a screen grab - np.asarray(ImageGrab.grab())[:,:,::-1].copy()
    TEMPLATE = Image('C:\\dev\\python\\rbot\\images\\template.bmp').mat

    def __init__(self):
        self._images = self._get_images()
        self._match_results = {}

    def _get_images(self):
        images = []

        for image_path in self._get_image_paths():
            image = Image(image_path)
            images.append(image)

        return images

    def _get_image_paths(self):
        abs_image_dir = self._resolve_root_image_dir()
        file_paths = []

        for file in listdir(abs_image_dir):
            file_paths.append(abs_image_dir + sep + file)

        return file_paths

    def _resolve_root_image_dir(self):
        relative_image_dir = 'images' + sep + 'buttons'
        absolute_image_dir = path.abspath(relative_image_dir)

        return absolute_image_dir

    def _match_all_images(self):
        for image in self._images:
            match_result = self._match(image)
            self._match_results[image] = match_result

    def _match(self, image):
        return matchTemplate(image.mat, ImageFinder.TEMPLATE, TM_CCOEFF)

    def find_images(self):
        # ToDo: focus game window before finding images
        self._match_all_images()

    def get_matched_images(self):
        return self._match_results.items()
