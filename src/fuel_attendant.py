from src.fuel import Fuel

class FuelAttendant:
    def __init__(self,attendant_name: str, dispenser):
        self.attendant_name = attendant_name
        self.dispenser = dispenser

    def add_fuel(self, fuel: Fuel):
         self.dispenser.add_fuel(fuel)

    def view_fuels(self):
        return self.dispenser.get_fuels()

    def dispenses_by_liters(self, fuel_name, liters):
        return self.dispenser.dispense_by_liters(fuel_name, liters)

    def dispenses_by_amount(self, fuel_name, amount):
        return self.dispenser.dispense_by_amount(fuel_name, amount)

    def update_fuel_price(self, fuel_name: str, new_price: float):
        fuel = self.dispenser.get_fuel(fuel_name)
        fuel.update_price(new_price)

    def

    def transactions(self):
        return self.dispenser.get_transactions()