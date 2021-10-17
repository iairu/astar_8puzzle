from enum import Enum
from array import array

class StateOperator(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

class State(object):

    def __init__(self, n: int, _elms: tuple):
        # todo later: cache position of 0 elm thorugh init args for quick access in operation()
        # todo later  \_ this way only init and fin states will have to be precalculated thru loops and operation() won't have to loop over elms to find the 0
        # todo later: cache manhattanSum as a tuple
        
        # create a hash from a tuple
        # hash is needed for set()
        
        # this can be easily achieved using the builtin Pyhton hash function and a string 
        # (which is directly hashable unlike this class or elms tuple)
        # the hash value changes between python runs, however its integrity remains intact between class instances
        h = ""
        for e in _elms:
            h += str(e) + "|"

        # actually properly generate and save the hash
        self._elms_hash = hash(h)

        # side length
        self.n = n

        # state elms must not be changed, that's why tuple (which is an immutable list)
        self.elms = _elms

        # defaults for unexplored directions
        self.left = None
        self.right = None
        self.up = None
        self.down = None

        return

    def __len__(self):
        # there isn't much else to measure here than the element count, might as well make it direct to the class
        return len(self.elms)

    def __hash__(self):
        # for set()
        return self._elms_hash

    def __eq__(self, _state: object) -> bool:
        # for set()
        return False if not isinstance(_state, State) else self.elms == _state.elms
