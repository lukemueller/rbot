from lib.client import Client
from lib.skill_bar import SkillBar
from util.runnable_factory import RunnableFactory
from util.window_handle import WindowHandle


class Bot():

    def __init__(self, prompter):
        self._prompter = prompter
        self._prompter.start()
        self._last_client = None
        self._clients = \
            self._generate_clients()
        self._runnable_to_client_map = \
            self._get_runnable_to_client_map()
        self._sorted_by_priority_runnables = \
            self._get_sorted_by_priority_runnables()

    def start(self):
        while True:
            runnable = self._get_next_runnable()
            client = self._runnable_to_client_map[runnable]
            should_focus = client is not self._last_client
            client.run(runnable, should_focus)
            self._last_client = client

    def _get_taskbar_coords(self, character_index):
        return (260+(character_index*200), 1070)

    def _generate_clients(self):
        clients = []
        for character in self._prompter.characters:
            clients.append(self._generate_client(
                character,
                self._get_taskbar_coords(len(clients))))

        return clients

    def _generate_client(self, character, taskbar_coords):
        runnables = RunnableFactory(character).generate_runnables()
        window_handle = WindowHandle(character.index, taskbar_coords)

        return Client(runnables, SkillBar(), window_handle)

    def _get_runnable_to_client_map(self):
        runnable_to_client_map = {}
        for client in self._clients:
            for runnable in client.runnables:
                runnable_to_client_map[runnable] = client

        return runnable_to_client_map

    def _get_sorted_by_priority_runnables(self):
        return sorted(
            self._runnable_to_client_map.keys(),
            key=lambda runnable: runnable.priority)

    def _get_next_runnable(self):
        next_runnable = None

        for runnable in self._sorted_by_priority_runnables:
            if runnable.needs_to_run():
                next_runnable = runnable
                break

        return next_runnable
