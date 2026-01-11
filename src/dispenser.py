from src.exceptions import InvalidDispenseValueError


class Dispenser:
    def __init__(self):
        self._fuels = {}
        self._transactions = []

    def add_fuel(self,fuel):
        self._fuels[fuel.name] = fuel

    def dispense_by_liters(self, fuel_name: str, liters: float):
        if liters < 1 or liters > 50:
            raise InvalidDispenseValueError()

