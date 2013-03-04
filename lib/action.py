from autopy import key

class Action():

    KEY_MAP = { 'F1':key.K_F1, 'F2':key.K_F2, 'F3':key.K_F3, 'F4':key.K_F4, 'F5':key.K_F5, 'F6':key.K_F6,
                'F7':key.K_F7, 'F8':key.K_F8, 'F9':key.K_F9, 'F10':key.K_F10, 'F11':key.K_F11, 'F12':key.K_F12
    }

    def __init__(self, name, coords):
        self.name = name
        self.coords = coords
        self.key_binding = None

    def set_key_binding(self, key):
        self.key_binding = Action.KEY_MAP[key]
