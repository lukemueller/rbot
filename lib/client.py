from time import sleep
from autopy import mouse


class Client():

    def __init__(self, runnables, pwa_app, window_handle, taskbar_coords):
        self._runnables = runnables
        self._window = self._get_window(pwa_app, window_handle)
        self._taskbar_coords = taskbar_coords

    def _get_window(self, pwa_app, handle):
        return pwa_app.window_(handle=handle)

    def initialize(self):
        # @ToDo: runnable init just inits the skillbar which only needs to be done once
        self.set_focus()
        for runnable in self._runnables:
            runnable.initialize()

    def set_focus(self):
        # self._toggle_window.SetFocus()
        # self._window.SetFocus()
        mouse.move(self._taskbar_coords[0], self._taskbar_coords[1])
        mouse.click()
        sleep(1)

    def run(self, runnable, focus=True):
        if focus:
            self.set_focus()

        runnable.run()

    def get_run_info(self):
        runnable_info = []

        for runnable in self._runnables:
            info_tuple = (self, runnable, runnable.should_run(), runnable.get_priority())
            runnable_info.append(info_tuple)

        return runnable_info
