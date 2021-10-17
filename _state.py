
from array import array

class State:

    def __init__(self, _elms: array):
        self.elms = _elms
        return

    def __len__(self):
        return len(self.elms)