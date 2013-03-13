from autopy import mouse, key
from time import sleep


class SkillBar():

    def __init__(self):
        self._action_map = None

    def do_action(self, action):
        if action.preferred_method is 'key':
            self._do_action_by_key(action)
        else:
            self._do_action_with_mouse(action)
        sleep(float(action.pause))

    def _move_mouse(self, coords):
        mouse.move(coords[0], coords[1])

    def _double_click(self):
        mouse.click()
        mouse.click()

    def _do_action_by_key(self, action):
        key.tap(action.key_binding)

    def _do_action_with_mouse(self, action):
        self._move_mouse(action.coords)
        self._double_click()
