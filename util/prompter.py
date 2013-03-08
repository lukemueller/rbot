from os import listdir, path


class Prompter():

    def __init__(self):
        self._config_path = self._resolve_config_path()
        self._roles = []
        self._options = self._get_options()
        self.results = []

    def _resolve_config_path(self):
        return path.abspath('config')

    def _get_options(self):
        options = {}
        for role in self._get_roles():
            tasks = self._get_tasks_for_role(role)
            options[role] = tasks

        return options

    def _get_roles(self):
        self._roles = listdir(self._config_path)
        return self._roles

    def _get_tasks_for_role(self, role):
        return listdir(path.join(self._config_path, role))

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
        self._get_results()
