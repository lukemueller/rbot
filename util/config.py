from os import path, sep


class Config():

    def __init__(self, role, task):
        self.role = role
        self.task = task
        self._path = self._resolve_path()
        self.cycle_time = None
        self.actions = self._map_actions()

    def _resolve_path(self):
        relative_path = 'config' + sep + self.role + sep + self.task + '.cfg'
        return path.abspath(relative_path)

    def _map_actions(self):
        config = open(self._path, 'r')
        lines = config.readlines()
        config.close()

        try:
            self.cycle_time = int(lines[0].rstrip())
        except ValueError:
            self.cycle_time = lines[0].rstrip()

        actions = {}
        for line in lines[1:]:
            line = line.rstrip()
            action_name, sleep = line.split(' ')
            actions[action_name] = sleep

        return actions
