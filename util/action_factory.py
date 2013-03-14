# from lib.action import Action
# import numpy as np


# class ActionsFactory():
#     OFFSET = 15
#     KEYS = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12']

#     def __init__(self, finder, task):
#         self._finder = finder
#         self._task = task
#         self._actions = []

#     def _get_raw_coordinates(self, match_result):
#         return np.unravel_index(match_result.argmax(), match_result.shape)

#     def _adjust_coordinates(self, numpy_coords):
#         x = int(numpy_coords[1])
#         y = int(numpy_coords[0])

#         return (x+ActionsFactory.OFFSET, y+ActionsFactory.OFFSET)

#     def _generate_action(self, image, match_result):
#         raw_coords = self._get_raw_coordinates(match_result)
#         adjusted_coords = self._adjust_coordinates(raw_coords)
#         action = Action(image.name, adjusted_coords)

#         self._actions.append(action)

#     def _map_keys(self):
#         # ToDo - this algorithm needs to be way better.
#         #        Currently it will only correctly map actions on the skillbar
#         #        that are sequential on the bottom row and have a matching button
#         sorted_by_x = sorted(self._actions, key=lambda action: action.coords[0])

#         for index in range(len(sorted_by_x)):
#             sorted_by_x[index].set_key_binding(ActionsFactory.KEYS[index])

#     def generate_actions_from_match_results(self):
#         for image, match_result in self._finder.get_matched_images():
#             self._generate_action(image, match_result)

#         self._map_keys()

#         return self._actions

#     def generate_actions_from_task(self):
#         for tuple in self._task.actions:
#             action_name, key, pause = tuple
#             action = Action(action_name, None, 'key', pause)
#             action.set_key_binding(key)
#             self._actions.append(action)

#         return self._actions
