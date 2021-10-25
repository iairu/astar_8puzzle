from _state import StateOperator

class FinSequence:
    def __init__(self, price: int):
        # first value (after reversing) will be price (depth)
        # followed by a StateOperation sequence that lead to the final state from init state
        self.seq = [price]
        self.reversed = False
        return

    def append(self, op: str):
        self.seq.append(op) # in place
        return self

    def reverse(self):
        if (self.reversed):
            return self
        self.seq.reverse() # in place
        self.reversed = True
        return self

    def __str__(self) -> str:
        # for ugly print()
        return str(self.seq)

    def print(self, _full: bool = True):
        # for pretty print
        # _full print also includes directions taken printed out

        # for first oldest ordering list must be reversed
        # because recursion return appending took place at the end not beginning
        if not (self.reversed):
            self.reverse()

        # full or partial print generation
        out = ""
        if (_full):
            for op in self.seq:
                if isinstance(op, StateOperator):
                    if (op == StateOperator.LEFT):
                        out += "L"
                    elif (op == StateOperator.RIGHT):
                        out += "R"
                    elif (op == StateOperator.UP):
                        out += "U"
                    elif (op == StateOperator.DOWN):
                        out += "D"
                elif isinstance(op,int):
                    out += "\nFinal state found in depth of " + str(op)
        else:
            last = self.seq[len(self.seq) - 1]
            if isinstance(last,int):
                out = "Final state found in depth of " + str(last)
        
        # printout
        print(out)
        return