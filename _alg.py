from _math import *
from _state import *
from _direction import *
from _seq import *

class AStar:
    def manhattanSum(_from: State, _to: State) -> int:
        # exponential difficulty
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
        # linear difficulty
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

    # ---------------------------------

    def explore(_from: State, _to: State, _rec_limit: int = 1000, _print: int = 2):
        # Public exploration function with a recursion limit
        # returns based on internal __explore__ function

        # Call internal function and get variable result
        explored = AStar.__explore__(_from, _to, _rec_limit)

        # Printing depending on result
        if (_print > 0):
            if (explored == None):
                print("No solution found. Recursion limit reached.")
            elif isinstance(explored,FinSequence):
                explored.print(True if (_print > 1) else False)
            elif isinstance(explored,set):
                print("No solution possible. All possible states explored.")

        return explored

    def __explore__(_from: State, _to: State, _rec_limit: int, g: int = None, h: int = None, states: set = None):
        # Internal exploration function - The A* algorithm

        # returns sequence of ops if final found (tried to return list but it misidentified it as a set)
        # otherwise returns set of explored states (if all possible states explored and no solution found)
        # can also return None if recursion limit reached

        # CHECKS AND DEFAULTS

        # if final state return FinSequence, first value will be price
        if (_from.elms == _to.elms):
            return FinSequence(g)

        # recursion limit check
        if (_rec_limit <= 0):
            return None

        # existing states that if reached again won't be considered by the algorithm
        # no need to include the final state, because once it will be reached the algorithm will end successfuly
        if (states == None):
            states = set() # set of explored states to avoid infinite loop
        states.add(_from)

        # tree depth for A*
        if (g == None): 
            g = 0 # root depth price
        g_next = g + 1 # next depth price

        # manhattan for A*
        if (h == None):
            h = AStar.manhattanSum(_from, _to) # default manhattan sum from _from to _to

        # for sorting after generation
        directions = []

        # STATE EXPANSION USING OPS & EXPLORATION

        # generation, price calculation, sorting
        left = _from.operation(StateOperator.LEFT)
        if (left != None and left not in states):
            h_left = h + AStar.manhattanDelta(left, _to) # next manhattan sum
            c_left = g_next + h_left
            directions.append(Direction(c_left, StateOperator.LEFT))

        right = _from.operation(StateOperator.RIGHT)
        if (right != None and right not in states):
            h_right = h + AStar.manhattanDelta(right, _to)
            c_right = g_next + h_right
            directions.append(Direction(c_right, StateOperator.RIGHT))

        up = _from.operation(StateOperator.UP)
        if (up != None and up not in states):
                h_up = h + AStar.manhattanDelta(up, _to)
                c_up = g_next + h_up
                directions.append(Direction(c_up, StateOperator.UP))

        down = _from.operation(StateOperator.DOWN)
        if (down != None and down not in states):
            h_down = h + AStar.manhattanDelta(down, _to)
            c_down = g_next + h_down
            directions.append(Direction(c_down, StateOperator.DOWN))

        # Sort all of the possible directions
        directions.sort()

        # Explore sorted states (cheapest first)
        for d in directions:
            if isinstance(d, Direction):
                # Explore in the correct direction
                if (d.operation == StateOperator.LEFT):
                    ret = AStar.__explore__(left, _to, _rec_limit - 1, g_next, h_left, states)
                elif (d.operation == StateOperator.RIGHT):
                    ret = AStar.__explore__(right, _to, _rec_limit - 1, g_next, h_right, states)
                elif (d.operation == StateOperator.UP):
                    ret = AStar.__explore__(up, _to, _rec_limit - 1, g_next, h_up, states)
                elif (d.operation == StateOperator.DOWN):
                    ret = AStar.__explore__(down, _to, _rec_limit - 1, g_next, h_down, states)

                # If exploration yields final state, return sequence of directions (backwards!)
                if isinstance(ret, FinSequence):
                    return ret.append(d.operation) # FinSequence append

        # Next direction's exploration needs to be aware of the last's exploration
        return states