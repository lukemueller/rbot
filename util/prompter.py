from threading import Thread


class Prompter(Thread):

	def __init__(self):
		Thread.__init__(self)
		self._ready = False
		self._tasks = ['farm', 'suspend', 'exit']
		self._task = None
		self._roles = ['visitor']
		self._role = None

	def run(self):
		# Get initial role
		self._role = self._get_from_prompt("Select character class:\n", self._roles)
		# Get inital task
		self._task = self._get_from_prompt("Pick a task:\n", self._tasks)
		# Set state to ready for main bot
		self._ready = True

		# Listen for task changes
		while(True):
			self._get_from_prompt("Pick a task:\n", self._tasks)

	def _get_from_prompt(self, prompt_header, prompt_options):
		# doesnt look like passing in an instace var is working
		prompt_message = self._generate_prompt(prompt_header, prompt_options)
		prompt_result_index = self._prompt(prompt_message)

		return prompt_options[prompt_result_index]

	def _prompt(self, message):
		prompt_index = None

		while type(prompt_index) is not int:
			input = raw_input(message)
			try:
				prompt_index = int(input)-1
			except ValueError:
				print "Input must be a number"

		return prompt_index

	def _generate_prompt(self, header, options):
		prompt = header

		for index in range(len(options)):
			prompt += "\t(%s) %s\n" % (index+1, options[index])
		prompt += "\t"

		return prompt

	def is_initializing(self):
		return not self._ready

	def current_role(self):
		return self._role

	def current_task(self):
		return self._task