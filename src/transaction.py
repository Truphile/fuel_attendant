from datetime import datetime

import datetime


class Transaction:
    def __init__(self,fuel_name: str,liters: float,amount: float):
        self.fuel_name = fuel_name
        self.liters = liters
        self.amount = amount
        self.timestamp = datetime.datetime.now()

    def receipt(self) -> str :
        return (
                f"Fuel: {self.fuel_name}\n" 
                f"Liters: {self.liters:.2f}L\n" 
                f"Amount: {self.amount:.2f}\n" 
                f"Time: {self.timestamp}"
        )
