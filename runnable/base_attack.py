from autopy import *


class BaseAttack():

    def __init__(self, buttons):
        self._buttons = buttons

    def do_action(action, pause=0):
        coords = self._get_coords(action)
        self._move_mouse(coords)
        self._double_click()
        sleep(pause)

    def spam_pickup(self, count=1):
        coords = self._get_coords("pickup")
        self._move_mouse(coords)

        for x in range(count):
            self._double_click("pickup", 2)

    def _move_mouse(self, coords):
        mouse.move(coords[0], coords[1])

    def _double_click(self, action):
        mouse.click()
        mouse.click()

    def _get_coords(self, action):
        return self._buttons.get(action)
