from src.exceptions import InvalidDispenseValueError,FuelNameNotFoundError,InsufficientFuelQuantityError
from src.transaction import Transaction
from src.fuel import Fuel

class Dispenser:

    Max_DISPENSER_LITERS = 50.00

    def __init__(self):
        self._fuels = {}
        self._transactions = []

    def add_fuel(self,fuel):
        self._fuels[fuel.name.lower()] = fuel

    def get_fuels(self):
        return self._fuels.values()

    def get_fuel(self, fuel_name: str):
        fuel = self._fuels.get(fuel_name.lower())
        if not fuel:
            raise FuelNameNotFoundError(f"Fuel {fuel_name} not found")
        return fuel


    def dispense_by_liters(self, fuel_name: str, liters: float):
        if not (1 <= liters <= self.Max_DISPENSER_LITERS):
            raise InvalidDispenseValueError(f"Dispense value must be between 1 and 50 ")

        fuel = self.get_fuel(fuel_name)


        if liters > fuel.quantity:
            raise InsufficientFuelQuantityError()


        amount = liters * fuel.price_per_liter
        fuel.dispense(liters)

        tranx = Transaction(fuel_name, liters, amount)
        self._transactions.append(tranx)
        return tranx

    def dispense_by_amount(self, fuel_name: str, amount: float):
        fuel = self.get_fuel(fuel_name)

        if amount < fuel.price_per_liter:
            raise InvalidDispenseValueError(f"Amount is less than {fuel.price_per_liter}")

        liters = amount / fuel.price_per_liter

        if liters > fuel.quantity:
            raise InsufficientFuelQuantityError()

        fuel.dispense(liters)

        tranx = Transaction(fuel_name, liters, amount)
        self._transactions.append(tranx)
        return tranx

    def get_transactions(self):
        return self._transactions



