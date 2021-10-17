from _math import *
from _state import State

class AStar:
    def manhattanSum(_from: State, _to: State, n: int) -> int:
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