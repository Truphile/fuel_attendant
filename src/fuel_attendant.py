class FuelAttendant:
    def __init__(self,attendant_name: str, dispenser):
        self.attendant_name = attendant_name
        self.dispenser = dispenser

    def view_fuels(self):
        return self.dispenser.get_fuels()