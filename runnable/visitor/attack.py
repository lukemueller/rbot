from runnable.base_attack import BaseAttack


class Attack(BaseAttack):

    def run(self):
        self.do_action("target")
        self.do_action("attack", 8)
        self.spam_pickup(2)
