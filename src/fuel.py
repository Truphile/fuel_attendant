class Fuel:

    def __init__(self, name: str, price_per_liter: float, quantity: float):
        if price_per_liter <= 0 or quantity <= 0:
            raise ValueError("Price per liter and quantity must be positive")

        self.name = name
        self.quantity = quantity
        self.price_per_liter = price_per_liter
