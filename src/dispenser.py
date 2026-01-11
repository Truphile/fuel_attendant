class Dispenser:
    def __init__(self):
        self._fuels = {}
        self._transactions = []

    def add_fuel(self,fuel):
        self._fuels[fuel.name] = fuel

