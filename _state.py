from enum import Enum
from array import array

class StateOperator(Enum):
    # defined as delta [column, row] of position
    # todo: if diagonal directions would ever be considered, it would be useful to turn it into a price as well
    NONE = [0,0] # default for initialization, init and final states
    LEFT = [-1,0]
    RIGHT = [1,0]
    UP = [0,-1]
    DOWN = [0,1]

class State(object):

    def __init__(self, n: int, _elms: list):
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

        # state elms
        # python by default makes list copies shallow which made me lose an hour of my life debugging
        self.elms = []
        for elm in _elms: # non-shallow copy
            self.elms.append(elm)

        # defaults for unexplored directions
        self.left = None
        self.right = None
        self.up = None
        self.down = None

        # # price for choosing the cheapest state (sorting)
        # self.price = -1

        # delta compared to parent state, because every state only 1 elm moves
        # this is to directly identify it for manhattanDelta(), so that the whole manhattanSum() doesn't need
        # to be recalculated from scratch

        self.mdelta = StateOperator.NONE # state operator used over parent to generate this state
        self.mpos = None # position of moved elements
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

    # def __lt__(self, _state):
    #     # for sort()
    #     if (self.price == -1):
    #         return False # invalid price
    #     return self.price < _state.price

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

        # elms that will be modified to generate a new state
        # can't use elms = self.elms because it would be shallow
        elms = []

        # find 0
        # also copy elms from self.elms
        zcol = -1
        zrow = -1
        for ei, ev in enumerate(self.elms):
            elms.append(ev)
            if (ev == 0):
                zrow = int(ei / n)
                zcol = ei % n
        # assert (zcol == -1 or zrow == -1), "There is no 0 in the current state" # already checked in main, maybe delete?

        # conclude operation based on operator enum over 0 and relevant elm next to it
        # mrow/mcol/mpos = modified row/column/position
        # zrow/zcol/zpos = zero row/column/position
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
                self.left.mpos = zpos # zpos is now mpos
                self.left.mdelta = StateOperator.LEFT # -1;0
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
                self.right.mpos = zpos
                self.right.mdelta = StateOperator.RIGHT # 1;0
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
                self.up.mpos = zpos
                self.up.mdelta = StateOperator.UP # 0;-1
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
                self.down.mpos = zpos
                self.down.mdelta = StateOperator.DOWN # 0;1
                return self.down

        return None # unreachable unless error