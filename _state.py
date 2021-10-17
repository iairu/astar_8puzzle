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

    def __str__(self):
        # for print()
        s = ""
        n = self.n
        last = n * n - 1 # no new line at end of print
        for ei, ev in enumerate(self.elms):
            # output
            s += str(ev) + " "
            # newline calc
            if (ei < last and (ei + 1) % n == 0): s += "\n"
        return s


    def operation(self, operator: StateOperator):
        # return if already explored
        if (operator == StateOperator.LEFT and self.left != None):
            return self.left
        elif (operator == StateOperator.RIGHT and self.right != None):
            return self.right
        elif (operator == StateOperator.UP and self.up != None):
            return self.up
        elif (operator == StateOperator.DOWN and self.down != None):
            return self.down

        # side length
        n = self.n

        # find 0
        zcol = -1
        zrow = -1
        for ei, ev in enumerate(self.elms):
            if (ev == 0):
                zrow = int(ei / n)
                zcol = ei % n
                break
        # assert (zcol == -1 or zrow == -1), "There is no 0 in the current state" # already checked in main, maybe delete?

        # conclude operation based on operator enum over 0 and relevant elm next to it
        elms = array("i",self.elms)
        if (operator == StateOperator.LEFT):
            # mrow = zrow
            # mcol = zcol + 1
            if (zcol + 1 >= n): # same state, hit border
                self.left = None
                return None
            else:
                mpos = zrow * n + (zcol + 1)
                zpos = mpos - 1
                elms[zpos] = elms[mpos]
                elms[mpos] = 0
                self.left = State(n, elms)
                return self.left
        elif (operator == StateOperator.RIGHT):
            # mrow = zrow
            # mcol = zcol - 1
            if (zcol - 1 < 0): # same state, hit border
                self.right = None
                return None
            else:
                mpos = zrow * n + (zcol - 1)
                zpos = mpos + 1
                elms[zpos] = elms[mpos]
                elms[mpos] = 0
                self.right = State(n, elms)
                return self.right
        elif (operator == StateOperator.UP):
            # mrow = zrow + 1
            # mcol = zcol
            if (zrow + 1 >= n): # same state, hit border
                self.up = None
                return None
            else:
                mpos = (zrow + 1) * n + zcol
                zpos = mpos - n
                elms[zpos] = elms[mpos]
                elms[mpos] = 0
                self.up = State(n, elms)
                return self.up
        elif (operator == StateOperator.DOWN):
            # mrow = zrow - 1
            # mcol = zcol
            if (zrow - 1 < 0): # same state, hit border
                self.up = None
                return None
            else:
                mpos = (zrow - 1) * n + zcol
                zpos = mpos + n
                elms[zpos] = elms[mpos]
                elms[mpos] = 0
                self.down = State(n, elms)
                return self.down

        return None # unreachable unless error