class Task():

    def __init__(self, cycle_time, priority, actions):
        self.cycle_time = cycle_time
        self.priority = int(priority)
        self.actions = self._parse_actions(actions)

    def _parse_actions(self, raw_actions):
        actions = []

        for action_line in raw_actions:
            action_line = action_line.rstrip()
            action_name, key, sleep = action_line.split(' ')
            actions.append((action_name, key, sleep))

        return actions
