from _math import *
from _state import *
from _direction import *

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

    def explore(_from: State, _to: State, g: int = None, h: int = None, states: set = None):
        # Finally... THE ALGORITHM ITSELF

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

        print("FROM:")
        print(_from)

        print("TO:")
        print(_to)

        print(f"g, h = {g}, {h}")

        # for sorting after generation
        directions = []

        # generation, price calculation, sorting
        _from.operation(StateOperator.LEFT)
        if (_from.left != None and _from.left not in states):
            h_next = h + AStar.manhattanDelta(_from.left, _to) # next manhattan sum
            c_left = g_next + h_next
            print(f"Left: c ({c_left}) = g + h = ({g_next} + {h_next})")
            directions.append(Direction(c_left, StateOperator.LEFT))

        _from.operation(StateOperator.RIGHT)
        if (_from.right != None and _from.right not in states):
            h_next = h + AStar.manhattanDelta(_from.right, _to)
            c_right = g_next + h_next
            print(f"Right: c ({c_right}) = g + h = ({g_next} + {h_next})")
            directions.append(Direction(c_right, StateOperator.RIGHT))

        _from.operation(StateOperator.UP)
        if (_from.up != None and _from.up not in states):
            h_next = h + AStar.manhattanDelta(_from.up, _to)
            c_up = g_next + h_next
            print(f"Up: c ({c_up}) = g + h = ({g_next} + {h_next})")
            directions.append(Direction(c_up, StateOperator.UP))

        _from.operation(StateOperator.DOWN)
        if (_from.down != None and _from.down not in states):
            h_next = h + AStar.manhattanDelta(_from.down, _to)
            c_down = g_next + h_next
            print(f"Down: c ({c_down}) = g + h = ({g_next} + {h_next})")
            directions.append(Direction(c_down, StateOperator.DOWN))

        # Sort all of the possible directions
        directions.sort()

        # Explore sorted states
        print("States will be further explored in the following order:")
        for d in directions:
            if isinstance(d, Direction):
                print(f"{d.operation} (c = {d.price})")
                # todo explore until _to found
                #self.explore(_from.left, _to, g + 1, h + self.manhattanDelta(_from.left, _to), states)
                # todo: \_ for each of these make sure to "return states" as any newly added ones in say c_left will be useful for c_right and so on
                # todo: \_ the final sequence of operations necessary to get from _from to _to should just get saved in the AStar class, but for ...
                # todo: \_ ... that it needs to get initialized first and __init__ should have _from and _to as args, then they shouldn't be in explore()

