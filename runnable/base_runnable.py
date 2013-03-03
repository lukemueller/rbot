# Simple proxy class that delages to the skillbar public API
class BaseRunnable():

	def __init__(self, skill_bar):
		self._skill_bar = skill_bar

	def do_action_and_pause(self, action, pause):
		self._skill_bar.do_action_and_pause(action, pause)

	def do_action(self, action):
		self._skill_bar.do_action(action)

	def spam_pickup(self, count):
		self._skill_bar.spam_pickup(count)