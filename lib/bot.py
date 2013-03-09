from time import time
import pywinauto
from util.config import Config
from util.image_finder import ImageFinder
from lib.skill_bar import SkillBar
from lib.runnable import Runnable
from lib.client import Client


class Bot():

    def __init__(self, prompter):
        self._pwa_app = pywinauto.application.Application()
        self._prompter = prompter
        self._window_handles = self._get_windows()
        self._clients = []
        self.start()
        # Temp
        self._last_buff = None

    def _get_windows(self):
        handles = pywinauto.findwindows.find_windows(
            title=u'ROSE Online',
            class_name='classCLIENT')

        try:
            handles.reverse()
        except SyntaxError:
            handles = handles,

        return handles

    def _create_client(self, role, task, character_index):
        config = Config(role, task)
        image_finder = ImageFinder(config)
        skill_bar = SkillBar(image_finder)
        runnable = Runnable(skill_bar, config)

        client = Client(
            runnable,
            self._pwa_app,
            self._window_handles[character_index]).initialize()

        client.log()
        return client

    def _should_buff(self):
        # Temp
        time_since_last_buff = time() - self._last_buff
        return int(time_since_last_buff) > 900

    def start(self):
        self._prompter.start()

        character_count = 0
        for tuple in self._prompter.results:
            role, task = tuple
            self._clients.append(
                self._create_client(role, task, character_count))
            character_count += 1

        raider = self._clients[0]
        cleric = self._clients[1]

        # initial buff
        cleric.run()
        self._last_buff = time()

        while(True):
            # start leveling
            raider.run()

            #check buffs
            if self._should_buff():
                cleric.run()
                self._last_buff = time()
