import unittest

from src.transaction import Transaction


class MyTestCase(unittest.TestCase):

    def test_transaction_works_correctly(self):
        tranx = Transaction("petrol",10.0,7950.0)
        self.assertEqual(tranx.fuel_name,"petrol")
        self.assertEqual(tranx.liters,10.0)
        self.assertEqual(tranx.amount,7950.0)
        self.assertIsNotNone(tranx.timestamp)