from lib.skill_bar import SkillBar
from util.image_finder import ImageFinder


class Bot():

    def __init__(self, prompter):
        self.prompter = prompter

    def start(self):
        self.prompter.start()

        # Wait for prompter to get required initial information from user
        while(self.prompter.is_initializing()):
            pass

        skill_bar = SkillBar(ImageFinder())

        old_task = self.prompter.current_task()
        current_task = None

        module = self.prompter.current_task()
        klass = self._resolve_klass_name()

        runnable = None

        # Run until user exits
        while(self.prompter.current_task() is not 'exit'):
            if old_task is not current_task:
                module = self.prompter.current_task()
                klass = self._resolve_klass_name()

                exec("from runnable.%s.%s import %s" %
                    (self.prompter.current_role(), module, klass))
            
                exec("runnable = %s(skill_bar)" % klass)

            runnable.run()

            current_task = self.prompter.current_task()

        print 'program should exit here'

    def _resolve_klass_name(self):
        task = self.prompter.current_task()
        return task[0].capitalize() + task[1:]
