from runnable.base_runnable import BaseRunnable

class Farm(BaseRunnable):

	def run(self):
		self.do_action("target")
		self.do_action_and_pause("attack", 6)
		self.spam_pickup(2)
