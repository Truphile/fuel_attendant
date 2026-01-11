import unittest

from src.fuel import Fuel


class FuelTest(unittest.TestCase):

    def test_I_can_successfully_create_fuel (self):
        fuel = Fuel("petrol",795,20)
        self.assertEqual(fuel.name,"petrol")
        self.assertEqual(fuel.price_per_liter,795)
        self.assertEqual(fuel.quantity,20)


    def test_Invalid_price_throws_exception(self):
        with self.assertRaises(ValueError):
            Fuel("petrol",0,20)

    def test_invalid_quantity_throws_exception(self):
        with self.assertRaises(ValueError):
            Fuel("petrol",795,-5)

    def test_update_price(self):
        fuel = Fuel("petrol",795,20)
        fuel.update_price_per_liter(805)
        self.assertEqual(fuel.price_per_liter,805)


