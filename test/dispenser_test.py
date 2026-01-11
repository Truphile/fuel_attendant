import unittest

from src.dispenser import Dispenser
from src.exceptions import InvalidDispenseValueError
from src.fuel import Fuel



class DispenserTest(unittest.TestCase):

    def setUp(self):
        self.dispenser = Dispenser()
        self.dispenser.add_fuel(Fuel("petrol",795,10))

    def test_dispense_fuel_by_liters(self):
        tranx = self.dispenser.dispense_by_liters("petrol",5)
        self.assertEqual(tranx.amount,3975)

    def test_dispense_invalid_liters_raises_exception(self):
        with self.assertRaises(InvalidDispenseValueError):
            self.dispenser.dispense_by_liters("petrol",0)

