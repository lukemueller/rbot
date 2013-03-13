from os import listdir, path


class Prompter():

    def __init__(self):
        self._root_config_path = self._resolve_root_config_path()
        self._roles = []
        self._options = self._get_options()
        self.results = []

    def _resolve_root_config_path(self):
        return path.abspath('config')

    def _get_options(self):
        options = {}
        for role in self._get_roles():
            tasks = self._get_tasks_for_role(role)
            options[role] = tasks

        return options

    def _get_roles(self):
        self._roles = listdir(self._root_config_path)
        return self._roles

    def _get_tasks_for_role(self, role):
        tasks = []
        for task in listdir(path.join(self._root_config_path, role)):
            tasks.append(task.split('.')[0])

        return tasks

    def _get_results(self):
        character_count_prompt = \
            self._generate_prompt(
                'How many characters do you want to play?\n')
        character_count = self._prompt(character_count_prompt)

        for x in range(int(character_count)+1):
            role_index = self._prompt(
                self._generate_prompt(
                    "Select role for character %s\n" % x,
                    self._options.keys()))
            role = self._roles[int(role_index)]

            task_index = self._prompt(
                self._generate_prompt(
                    "Select task for character %s\n" % x,
                    self._options[role]))
            task = self._options[role][int(task_index)]

            self.results.append((role, task))

    def _generate_prompt(self, header, options=[]):
        prompt = header

        for index in range(len(options)):
            prompt += "\t(%s) %s\n" % (index+1, options[index])
        prompt += "\t"

        return prompt

    def _prompt(self, message):
        user_input = None

        while type(user_input) is not int:
            input = raw_input(message)
            try:
                user_input = int(input)-1
            except ValueError:
                print "Input must be a number"

        return user_input

    def start(self):
        print 'Welcome to rbot\n \
            Make sure your clients are logged in and in position\n \
            Launch your clients in the order you specify your characters\n\n'

        self._get_results()

        print '\n\n'
        for tuple in self.results:
            role, task = tuple
            print 'Running %s for %s' % (task, role)
