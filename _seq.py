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

    def print(self):
        # for pretty print
        if not (self.reversed):
            self.reverse()

        out = ""
        last_op = len(self.seq) - 2
        for i, op in enumerate(self.seq):
            if isinstance(op, StateOperator):
                if (op == StateOperator.LEFT):
                    out += "L"
                elif (op == StateOperator.RIGHT):
                    out += "R"
                elif (op == StateOperator.UP):
                    out += "U"
                elif (op == StateOperator.DOWN):
                    out += "D"

                # if (i < last_op):
                #     out += " -> "
            elif isinstance(op,int):
                out += "\nFinal state found in depth of " + str(op)
        
        print(out)
        return