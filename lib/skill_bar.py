from util.actions_factory import ActionsFactory
from autopy import mouse
from time import sleep

class SkillBar():

	def __init__(self, image_finder):
		self._action_map = self._map_actions_from_screen(image_finder)

	def _map_actions_from_screen(self, image_finder):
		image_finder.find_images()
		actions = ActionsFactory(image_finder).generate_actions()

		return self._map_actions(actions)

	def _map_actions(self, actions):
		action_map = {}

		for action in actions:
			action_map[action.name] = action

		return action_map

	def _move_mouse(self, coords):
		mouse.move(coords[0], coords[1])

	def _double_click(self):
		mouse.click()
		mouse.click()

	def _get_action(self, key):
		return self._action_map[key]

	def do_action_and_pause(self, action, pause):
		action = self._get_action(action)
		self._move_mouse(action.coords)
		self._double_click()
		sleep(pause)

	def do_action(self, action):
		self.do_action_and_pause(action, 0)

	def spam_pickup(self, count):
		for x in range(count):
			self.do_action_and_pause("pickup", 2)
