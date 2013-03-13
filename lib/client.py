class Client():

    def __init__(self, runnables, skillbar, window_handle):
        self._runnables = runnables
        self._skillbar = skillbar
        self._window_handle = window_handle

    def run(self, runnable, focus=True):
        if focus:
            self._window_handle.set_focus()

        runnable.run(self._skillbar)
