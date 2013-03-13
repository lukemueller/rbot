from autopy import key


class Action():

    KEY_MAP = {'F1': key.K_F1, 'F2': key.K_F2, 'F3': key.K_F3, 'F4': key.K_F4, 'F5': key.K_F5, 'F6': key.K_F6,
               'F7': key.K_F7, 'F8': key.K_F8, 'F9': 120, 'F10': key.K_F10, 'F11': key.K_F11, 'F12': key.K_F12}

    def __init__(self, name, raw_key, coords, pause=None, preferred_method='key'):
        self.name = name
        self.coords = coords
        self.key_binding = self._map_key_binding(raw_key)
        self.preferred_method = preferred_method
        self.pause = pause

    def _map_key_binding(self, key):
        self.key_binding = Action.KEY_MAP[key]
