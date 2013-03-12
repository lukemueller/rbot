import pywinauto
from time import sleep
from autopy import mouse

class Client():

    def __init__(self, runnable, pwa_app, window_handle, taskbar_coords):
        self._runnable = runnable
        self._window = self._get_window(pwa_app, window_handle)
        self._taskbar_coords = taskbar_coords

    def _get_window(self, pwa_app, handle):
        return pwa_app.window_(handle=handle)

    def initialize(self):
        self.set_focus()
        self._runnable.initialize()

    def set_focus(self):
        # self._toggle_window.SetFocus()
        # self._window.SetFocus()
        mouse.move(self._taskbar_coords[0], self._taskbar_coords[1])
        mouse.click()
        sleep(1)

    def run(self, focus=True):
        if focus:
            self.set_focus()
        print "running %s for %s" %(self._runnable._config.task, self._runnable._config.role)
        self._runnable.run()

    def should_run(self):
        self._runnable.should_run()
