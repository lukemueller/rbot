from time import sleep
from autopy import mouse


class WindowHandle():

    def __init__(self, pwa_app, window_handle_id, taskbar_coords):
        self._window_handle = self._get_window_handle(pwa_app, window_handle_id)
        self._taskbar_coords = taskbar_coords

    def set_focus(self):
        if self._window is not None:
            self._set_focus_from_window_handle(self._window_handle)
        else:
            self._set_focus_from_taskbar_coords

    def _set_focus_from_taskbar_coords(self):
        x, y = self._taskbar_coords
        mouse.move(x, y)
        mouse.click()
        sleep(1)

    def _set_focus_from_window_handle(self):
        self._window_handle.SetFocus

    def _get_window_handle(self, pwa_app, window_handle_id):
        if pwa_app is not None and window_handle_id is not None:
            return pwa_app.window_(handle=handle)
        else:
            return False

        
