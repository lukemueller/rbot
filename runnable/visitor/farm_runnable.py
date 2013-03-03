from runnable.farm import Farm


class FarmRunnable(Farm):

	def run(self):
		self.do_action("target")
		self.do_action("attack", 6)
		self.spam_pickup(2)
