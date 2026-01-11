import unittest

from src.dispenser import Dispenser
from src.exceptions import (InvalidDispenseValueError, FuelNameNotFoundError, InsufficientFuelQuantityError)
from src.fuel import Fuel



class DispenserTest(unittest.TestCase):

    def setUp(self):
        self.dispenser = Dispenser()
        self.dispenser.add_fuel(Fuel("Petrol",795,10))

    def test_dispense_fuel_by_liters(self):
        tranx = self.dispenser.dispense_by_liters("Petrol",5)
        self.assertEqual(tranx.amount,3975)

    def test_dispense_too_many_liters_raises_exception(self):
        with self.assertRaises(InvalidDispenseValueError):
            self.dispenser.dispense_by_liters("petrol", 51)

    def test_dispense_invalid_liters_raises_exception(self):
        with self.assertRaises(InvalidDispenseValueError):
            self.dispenser.dispense_by_liters("Petrol",0)

    def test_dispense_fuel_not_found_raises_exception(self):
        with self.assertRaises(FuelNameNotFoundError):
            self.dispenser.dispense_by_liters("Aviation fuel",20)

    def test_dispense_insufficient_fuel_raises_exception(self):
        with self.assertRaises(InsufficientFuelQuantityError):
            self.dispenser.dispense_by_liters("Petrol",300)

    def test_dispense_by_amount(self):
        tranx = self.dispenser.dispense_by_amount("Petrol",4500)
        self.assertAlmostEqual(tranx.liters,5.66)

    def test_dispense_by_amount_works_correctly(self):
        tranx = self.dispenser.dispense_by_amount("Petrol", 1590)
        self.assertEqual(tranx.liters, 2)

    def test_transaction_recorded(self):
        self.dispenser.dispense_by_liters("Petrol", 5)
        self.assertEqual(len(self.dispenser.get_transactions()), 1)


