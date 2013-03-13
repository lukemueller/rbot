from time import time


class Runnable():

    def __init__(self, cycle_time, priority, actions):
        self.cycle_time = int(cycle_time)
        self.priority = priority
        self._actions = actions
        self._last_run = None

    def should_run(self):
        if self._last_run is None:
            return True

        time_since_last_run = time() - self._last_run
        return time_since_last_run > self.cycle_time

    def run(self, skillbar):
        for action in self._actions:
            skillbar.do_action(action)

        self._last_run = time()
