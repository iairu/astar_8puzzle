from _state import StateOperator

class Direction:
    def __init__(self, price: int, operation: StateOperator):
        self.operation = operation
        self.price = price
        return

    def __lt__(self, _direction):
        # for sort()
        return self.price < _direction.price