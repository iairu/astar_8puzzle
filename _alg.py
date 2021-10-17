from os import get_inheritable
from _math import *
from _state import *

class AStar:
    def manhattanSum(_from: State, _to: State) -> int:
        n = _from.n
        h = 0;
        for fi,fval in enumerate(_from.elms):
            if (fval == 0): continue # manhattan does not add empty field (X) to the sum
            delta = 0
            for ti, tval in enumerate(_to.elms):
                if (fval == tval): # found the same element, now calc delta
                    frow = int(fi / n)
                    fcol = fi % n
                    trow = int(ti / n)
                    tcol = ti % n

                    drow = absInt(trow - frow) # delta left / right
                    dcol = absInt(tcol - fcol) # delta up / down

                    delta = drow + dcol # delta up / down / left / right ONLY, no diagonals
                    break
            h += delta
        return h

    def manhattanDelta(_from: State, _to: State) -> int:
        n = _from.n
        delta = 0;
        fi = _from.mpos
        fval = _from.mval
        for ti, tval in enumerate(_to.elms):
            if (fval == tval): # found the same element, now calc delta
                frow = int(fi / n)
                fcol = fi % n
                trow = int(ti / n)
                tcol = ti % n

                drow = absInt(trow - frow) # delta left / right
                dcol = absInt(tcol - fcol) # delta up / down

                delta = drow + dcol # delta up / down / left / right ONLY, no diagonals
                break
        return delta

    def explore(_from: State, _to: State, _from_level: int = 0, states: set = None) -> set:
        # Finally... THE ALGORITHM ITSELF

        if (states == None):
            states = set() # set of explored states to avoid infinite loop
        elif (_from in states):
            return states # already explored
        else:
            states.add(_from)


        g_parent = _from_level
        h_parent = AStar.manhattanSum(_from, _to)
        c_parent = g_parent + h_parent # todo: where do i use this?


        _from.operation(StateOperator.LEFT)
        if (_from.left != None):
            g = _from_level + 1
            h = h_parent + AStar.manhattanDelta(_from.left,_to)
            c_left = g + h

        _from.operation(StateOperator.RIGHT)
        if (_from.right != None):
            g = _from_level + 1
            h = h_parent + AStar.manhattanDelta(_from.right,_to)
            c_right = g + h

        _from.operation(StateOperator.UP)
        if (_from.up != None):
            g = _from_level + 1
            h = h_parent + AStar.manhattanDelta(_from.up,_to)
            c_up = g + h

        _from.operation(StateOperator.DOWN)
        if (_from.down != None):
            g = _from_level + 1
            h = h_parent + AStar.manhattanDelta(_from.down,_to)
            c_down = g + h

        # todo comparison of c_left, right, up, down: order them lowest first, then explore until _to found
        # todo: \_ for each of these make sure to "return states" as any newly added ones in say c_left will be useful for c_right and so on
        # todo: \_ the final sequence of operations necessary to get from _from to _to should just get saved in the AStar class, but for ...
        # todo: \_ ... that it needs to get initialized first and __init__ should have _from and _to as args, then they shouldn't be in explore()
