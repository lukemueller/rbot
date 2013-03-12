from time import time
import pywinauto
from util.config import Config
from util.image_finder import ImageFinder
from lib.skill_bar import SkillBar
from lib.runnable import Runnable
from lib.client import Client


class Bot():

    PWA_APP = pywinauto.application.Application()

    def __init__(self, prompter):
        self._prompter = prompter
        self._window_handles = self._get_windows()
        self._toggle_window = self._get_toggle_window()
        self._clients = []
        self.start()
        # Temp
        self._last_buff = None

    def _get_toggle_window(self):
        w_handle = pywinauto.findwindows.find_windows(title=u'terminal - python main.py', class_name='ConsoleWindowClass')[0]
        return Bot.PWA_APP.window_(handle=w_handle)

    def _get_windows(self):
        handles = pywinauto.findwindows.find_windows(
            title=u'ROSE Online',
            class_name='classCLIENT')

        try:
            handles.reverse()
        except SyntaxError:
            handles = handles,

        return handles

    def _create_client(self, role, task, character_index, coords):
        config = Config(role, task)
        # image_finder = ImageFinder(config)
        image_finder = None
        skill_bar = SkillBar(image_finder)
        runnable = Runnable(skill_bar, config)

        return Client(
            runnable,
            Bot.PWA_APP,
            self._window_handles[character_index],
            coords)

    def _should_buff(self):
        # Temp
        time_since_last_buff = time() - self._last_buff
        return int(time_since_last_buff) > 800

    def start(self):
        self._prompter.start()

        character_count = 0
        x = 260
        y = 1070
        for tuple in self._prompter.results:
            role, task = tuple
            coords = (x, y)
            client = self._create_client(role, task, character_count, coords)
            client.initialize()
            self._clients.append(client)
            character_count += 1
            x += 200 

        raider = self._clients[0]
        cleric = self._clients[1]

        # initial buff
        cleric.run(False)
        self._last_buff = time()

        raider.run(True)

        while(True):
            # start leveling
            raider.run(False)

            #check buffs
            if self._should_buff():
                cleric.run()
                self._last_buff = time()
                raider.run()
