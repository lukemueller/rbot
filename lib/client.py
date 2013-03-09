class Client():

    def __init__(self, runnable, pwa_app, window_handle):
        self._runnable = runnable
        self._window = self._get_window(pwa_app, window_handle)

    def _get_window(self, pwa_app, handle):
        return pwa_app.window_(handle=handle)

    def initialize(self):
        self.set_focus()
        self._runnable.initialize()
        return self

    def set_focus(self):
        self._window.SetFocus()

    def run(self):
        print "running %s for %s" %(self._runnable._config.task, self._runnable._config.role)
        self.set_focus()
        self._runnable.run()

    def should_run(self):
        self._runnable.should_run()

    def log(self):
        # Temp
        print "Successfully created client"
        print "\tRole: %s" % self._runnable._config.role
        print "\tTask: %s" % self._runnable._config.task
        print "\tMappings: "
        for action_name, instance in self._runnable._skill_bar._action_map.items():
            print "\t\t%s : %s"  % (action_name, instance.key_binding)
