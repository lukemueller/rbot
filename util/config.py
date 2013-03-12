from os import path, sep
from util.task import Task


class Config():

    def __init__(self, role, task):
        self.role = role
        self.task = task
        self._path = self._resolve_path()
        self.tasks = self._map_tasks()

    def _resolve_path(self):
        relative_path = 'config' + sep + self.role + sep + self.task + '.cfg'
        return path.abspath(relative_path)

    # def _map_actions(self):
    #     config = open(self._path, 'r')
    #     lines = config.readlines()
    #     config.close()

    #     self.cycle_time = int(lines[0].rstrip())

    #     actions = {}
    #     for line in lines[1:]:
    #         line = line.rstrip()
    #         action_name, sleep = line.split(' ')
    #         actions[action_name] = sleep

    #     return actions

    def _map_tasks(self):
        task_line_groups = self._get_task_line_groups()
        task_objects = []

        for task_lines in task_line_groups:
            task_objects.append(Task(task_lines[0], task_lines[1], task_lines[2:]))

        return task_objects

    def _get_task_line_groups(self):
        config_lines = self._get_config_file_lines()
        task_lines = []

        there_are_still_tasks = True
        while there_are_still_tasks:
            try:
                index = config_lines.index('\n')
                task_lines.append(config_lines[:index])
                config_lines = config_lines[index+1:]
            except ValueError:
                there_are_still_tasks = False

        return task_lines

    def _get_config_file_lines(self):
        config = open(self._path, 'r')
        lines = config.readlines()
        config.close()

        return lines
