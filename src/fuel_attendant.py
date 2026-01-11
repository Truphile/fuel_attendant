class FuelAttendant:
    def __init__(self,attendant_name: str, dispenser):
        self.attendant_name = attendant_name
        self.dispenser = dispenser

    def view_fuels(self):
        return self.dispenser.get_fuels()

    def dispenses_by_liters(self, fuel_name, liters):
        return self.dispenser.dispense_by_liters(fuel_name, liters)