from lib.mapper import Mapper
from lib.prompter import Prompter


class Bot():

    def __init__(self, prompter, mapper):
        self.prompter = prompter
        self.mapper = mapper
        

    def start_botting(self):
        self.prompter.start()

        # Wait for prompter to get required initial information from user
        while(self.prompter.is_initializing()):
            pass

        # Run until user exits
        while(self.prompter.current_task() is not 'exit'):
            module = self._resolve_module_name()
            klass = self._resolve_klass_name()

            import_statement = "from runnable.%s.%s import %s" % \
                                (self.prompter.current_role(), module, klass)

            exec(import_statement)

            runnable = None
            exec("runnable = %s(Mapper())" % klass)

            # runnable.start()
            runnable.run()

        print 'program should exit here'

    def _resolve_module_name(self):
        return self.prompter.current_task() + "_runnable"

    def _resolve_klass_name(self):
        task = self.prompter.current_task()
        return task[0].capitalize() + task[1:] + "Runnable"


prompter = Prompter()
mapper = Mapper()
rbot = Bot(prompter, mapper)
rbot.start_botting()
