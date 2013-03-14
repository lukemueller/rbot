from time import sleep
from autopy import mouse
import pywinauto


class WindowHandle():

    PWA_APP = pywinauto.application.Application()
    HANDLES = pywinauto.findwindows.find_windows(
        title=u'ROSE Online',
        class_name='classCLIENT').reverse()

    def __init__(self, character_index, taskbar_coords, focus_method='mouse'):
        self._focus_method = focus_method
        self._window_handle = self._get_window_handle(character_index)
        self._taskbar_coords = taskbar_coords

    def set_focus(self):
        if self._focus_method is 'os':
            self._set_focus_from_window_handle(self._window_handle)
        elif self._focus_method is 'mouse':
            self._set_focus_from_taskbar_coords()

    def _set_focus_from_taskbar_coords(self):
        x, y = self._taskbar_coords
        mouse.move(x, y)
        mouse.click()
        sleep(1)

    def _set_focus_from_window_handle(self):
        self._window_handle.SetFocus

    def _get_window_handle(self, character_index):
        if self._focus_method is 'os':
            return WindowHandle.PWA_APP.window_(
                handle=WindowHandle.HANDLES[character_index])
        elif self._focus_method is 'mouse':
            return None
