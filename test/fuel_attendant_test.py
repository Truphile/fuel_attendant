import unittest

from src.dispenser import Dispenser
from src.fuel import Fuel
from src.fuel_attendant import FuelAttendant


class AttendantTest(unittest.TestCase):

    def setUp(self):
        self.dispenser = Dispenser()
        self.dispenser.add_fuel(Fuel("Petrol", 650, 100))
        self.attendant = FuelAttendant("Segun", self.dispenser)

    def test_view_fuels_returns_all_available_fuels(self):
        fuels = list(self.attendant.view_fuels())
        self.assertEqual(len(fuels), 1)