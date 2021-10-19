from _math import *
from _state import *

class AStar:
    def manhattanSum(_from: State, _to: State) -> int:
        n = _from.n
        hsum = 0; # manhattan sum
        for fi,fval in enumerate(_from.elms):
            if (fval == 0): continue # manhattan does not add empty field (X) to the sum
            h = 0 # manhattan elm
            for ti, tval in enumerate(_to.elms):
                if (fval == tval): # found the same element, now calc delta
                    frow = int(fi / n)
                    fcol = fi % n
                    trow = int(ti / n)
                    tcol = ti % n

                    drow = absInt(trow - frow) # delta left / right
                    dcol = absInt(tcol - fcol) # delta up / down

                    h = drow + dcol # delta up / down / left / right ONLY, no diagonals
                    break
            hsum += h
        return hsum

    def manhattanDelta(_from: State, _to: State) -> int:
        n = _from.n
        delta = 0;

        # get ti (final position of moved element)
        fi = _from.mpos # current position of moved element
        fval = _from.elms[fi] # value of moved element
        for ti, tval in enumerate(_to.elms):
            if (fval == tval): # found the same element, now calc delta
                break

        frow = int(fi / n) # current row of moved element
        fcol = fi % n # current column of moved element

        # pfi = fi - _from.mdelta[0] - (_from.mdelta[1] * n) # previous position
        pfrow = frow - _from.mdelta.value[1] # previous row of moved element
        pfcol = fcol - _from.mdelta.value[0] # previous column of moved element
        
        trow = int(ti / n) # final row of moved element
        tcol = ti % n # final column of moved element

        h = absInt(tcol - fcol) + absInt(trow - frow) # manhattan current position to finish (fi)
        ph = absInt(tcol - pfcol) + absInt(trow - pfrow) # manhattan previous position to finish (pfi)
        delta = h - ph # manhattan delta of moved element to finish

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
