from datetime import datetime

import datetime


class Transaction:
    def __init__(self,fuel_name: str,liters: float,amount: float):
        self.fuel_name = fuel_name
        self.liters = liters
        self.amount = amount
        self.timestamp = datetime.datetime.now()