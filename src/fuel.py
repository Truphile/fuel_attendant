class Fuel:

    def __init__(self, name: str, price_per_liter: float, quantity: float):
        if price_per_liter <= 0 or quantity <= 0:
            raise ValueError("Price per liter and quantity must be positive")

        self.name = name
        self.quantity = quantity
        self.price_per_liter = price_per_liter

    def update_price_per_liter(self, new_price_per_liter: float):
        if new_price_per_liter <= 0:
            raise ValueError("invalid price_per_liter")
        self.price_per_liter = new_price_per_liter

    def restock(self, liter: float):
        if liter <= 0:
            raise ValueError("invalid liter amount")
        self.quantity += liter

    def dispenser(self, liter: float):
        if liter <= 0 or liter > self.quantity:
            raise ValueError("invalid liter amount")
        self.quantity -= liter

