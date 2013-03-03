from lib.action import Action
import numpy as np


class ActionsFactory():
    OFFSET = 15
    KEYS = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12']

    def __init__(self, finder):
        self._finder = finder
        self._actions = []

    def _get_raw_coordinates(self, match_result):
        return np.unravel_index(match_result.argmax(), match_result.shape)

    def _adjust_coordinates(self, numpy_coords):
        x = int(numpy_coords[1])
        y = int(numpy_coords[0])

        return (x+ActionsFactory.OFFSET, y+ActionsFactory.OFFSET)

    def _generate_action(self, image, match_result):
        raw_coords = self._get_raw_coordinates(match_result)
        adjusted_coords = self._adjust_coordinates(raw_coords)
        action = Action(image.name, adjusted_coords)

        self._actions.append(action)

    def _map_keys(self):
        sorted_by_x = sorted(self._actions, key=lambda action: self._actions.coords[0])

        for index in range(len(sorted_by_x)):
            sorted_by_x[index].key_binding = ActionsFactory.KEYS[index]

        for action in self._actions:
            print action.name, ": ", action.key_binding

    def generate_actions(self):
        for image, match_result in self._finder.get_matched_images():
            self._generate_action(image, match_result)

        # self._map_keys()

        return self._actions

