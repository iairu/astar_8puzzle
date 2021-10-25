from _state import *

class Direction:
    def __init__(self, price: int, operation: StateOperator, state: State, h: int, g: int):
        self.operation = operation
        self.price = price
        self.state = state
        self.h = h
        self.g = g
        return

    def __lt__(self, _direction):
        # for sort()
        return self.price < _direction.price