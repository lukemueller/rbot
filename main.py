from lib.mapper import Mapper


class Bot():

    def __init__(self):
        self.mapper = Mapper()
        self.run()

    def run(self):
        role = self._get_role()
        task = self._get_task()

        klass = task[0].capitalize() + task[1:]
        runnable = __import__("runnable.%s.%s.%s" % role, task, klass)

        while(True):
            runnable(self.mapper).run()

    def _get_role(self):
        roles = ['visitor']
        prompt = self.generate_prompt("Select character class:\n", roles)
        prompt_index = raw_input(prompt)

        return roles[int(prompt_index)-1]

    def _get_task(self):
        tasks = ['attack']
        prompt = self.generate_prompt("Pick a task:\n", tasks)
        prompt_index = raw_input(prompt)

        return tasks[int(prompt_index)-1]

    def _generate_prompt(self, header, options):
        prompt = header
        for option in options:
            prompt += "(%i) %s" % options.index(option)+1, option

Bot()
