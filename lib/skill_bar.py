from util.actions_factory import ActionsFactory
from autopy import mouse, key
from time import sleep


class SkillBar():

    def __init__(self, image_finder):
        self._image_finder = image_finder
        self._action_map = None

    def _map_actions_from_screen(self):
        self._image_finder.initialize()
        actions = ActionsFactory(self._image_finder, None).generate_actions_from_match_results()

        return self._map_actions(actions)

    def _map_actions_from_task(self, task):
        actions = ActionsFactory(None, task).generate_actions_from_task()
        return self._map_actions(actions)

    def _map_actions(self, actions):
        action_map = {}

        for action in actions:
            action_map[action.name] = action

        return action_map

    def _move_mouse(self, coords):
        mouse.move(coords[0], coords[1])

    def _double_click(self):
        mouse.click()
        mouse.click()

    def _get_action(self, key):
        return self._action_map[key]

    def _do_action_by_key(self, action):
        key.tap(action.key_binding)

    def _do_action_with_mouse(self, action):
        self._move_mouse(action.coords)
        self._double_click()

    def initialize_with_image_finder(self):
        self._action_map = self._map_actions_from_screen()

    def initialize_with_config(self, config):
        self._action_map = self._map_actions_from_config(config)

    def do_action(self, action_name):
        action = self._get_action(action_name)

        if action.preferred_method is 'key':
            self._do_action_by_key(action)
        else:
            self._do_action_with_mouse(action)
        sleep(float(action.pause))
