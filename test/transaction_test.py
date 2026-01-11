import unittest

from src.transaction import Transaction


class MyTestCase(unittest.TestCase):

    def test_transaction_works_correctly(self):
        tranx = Transaction("petrol",10.0,7950.0)
        self.assertEqual(tranx.fuel_name,"petrol")
        self.assertEqual(tranx.liters,10.0)
        self.assertEqual(tranx.amount,7950.0)
        self.assertIsNotNone(tranx.timestamp)


    def test_receipt_format_works(self):
        tranx = Transaction("petrol",10.0,7950.0)
        receipt = tranx.receipt()

        self.assertIn("petrol",receipt)
        self.assertIn("10.00L",receipt)
        self.assertIn("7950.00",receipt)