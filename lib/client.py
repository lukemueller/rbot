class Client():

    def __init__(self, runnable):
        self._runnable = runnable
        self._window = window

    def initialize(self):
        self.set_focus()
        self._runnable.initialize()
        return self

    def set_focus(self):
        self._window.SetFocus()

    def run(self):
        self.set_focus()
        self._runnable.run()

    def should_run(self):
        self._runnable.should_run()