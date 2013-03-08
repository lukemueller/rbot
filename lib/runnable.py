from time import time


class Runnable():

    def __init__(self, skill_bar, config):
        self._config = config
        self._skill_bar = skill_bar
        self._last_run = None

    def initialize(self):
        self._skill_bar.set_up_from_focused_screen()

    def should_run(self):
        time_since_last_run = time() - self._last_run
        return time_since_last_run > int(self._config.cycle_time)

    def run(self):
        self._last_run = time()
        for action_name, pause in self._config.actions.items():
            self._skill_bar.do_action(action_name, pause)
