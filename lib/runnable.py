from time import time


class Runnable():

    def __init__(self, skill_bar, task):
        self._task = task
        self._skill_bar = skill_bar
        self._last_run = None

    def initialize(self):
        self._skill_bar.initialize_with_task(self._task)

    def should_run(self):
        time_since_last_run = time() - self._last_run
        return time_since_last_run > int(self._task.cycle_time)

    def run(self):
        self._last_run = time()
        for tuple in self._task.actions:
            self._skill_bar.do_action(tuple[0])

    def get_priority(self):
        return self._task.priority
