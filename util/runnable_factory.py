from os import path, sep
from lib.action import Action
from lib.runnable import Runnable


class RunnableFactory():

    def __init__(self, character):
        self.role = character.role
        self.task = character.task
        self._config_path = self._get_config_path()

    def generate_runnables(self):
        line_groups = self._get_grouped_lines()
        runnables = []

        for group in line_groups:
            cycle_time, priority = self._get_cycle_time_and_priority_from_line_group_in_config(group)
            actions = []
            for line in group[2:]:
                actions.append(self._generate_action_from_line_in_config(line))

            runnables.append(Runnable(cycle_time, priority, actions))

        return runnables

    def _get_cycle_time_and_priority_from_line_group_in_config(self, line_group):
        return (line_group[0], line_group[1])

    def _generate_action_from_line_in_config(self, line):
        action_name, key, pause = line.rstrip().split(' ')
        return Action(action_name, key, None, pause)

    def _get_config_path(self):
        relative_path = 'config' + sep + self.role + sep + self.task + '.cfg'
        return path.abspath(relative_path)

    def _get_grouped_lines(self):
        config_lines = self._read_config_file()
        grouped_lines = []

        there_are_still_tasks = True
        while there_are_still_tasks:
            try:
                index = config_lines.index('\n')
                grouped_lines.append(config_lines[:index])
                config_lines = config_lines[index+1:]
            except ValueError:
                there_are_still_tasks = False

        return grouped_lines

    def _read_config_file(self):
        config = open(self._config_path, 'r')
        lines = config.readlines()
        config.close()

        return lines
