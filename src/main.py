from src.fuel import Fuel
from src.dispenser import Dispenser
from src.fuel_attendant import FuelAttendant
from src.exceptions import (
    InsufficientFuelQuantityError,
    InvalidDispenseValueError, FuelNameNotFoundError
)


def display_menu():
    print("\n=== MULTI FUEL DISPENSER SYSTEM ===")
    print("1. View Available Fuels")
    print("2. Add New Fuel")
    print("3. Update Fuel Price")
    print("4. Restock Fuel")
    print("5. Dispense Fuel by Liters")
    print("6. Dispense Fuel by Amount")
    print("7. View Transactions")
    print("0. Exit")


def get_menu_choice():
    while True:
        choice = input("Select option: ").strip()
        if choice.isdigit():
            return choice
        print("Menu option must be a number.")


def get_alpha_string(prompt):
    while True:
        value = input(prompt).strip()
        if not value:
            print("Input cannot be empty.")
        elif not value.isalpha():
            print("Only letters are allowed.")
        else:
            return value


def get_numeric_value(prompt):
    while True:
        value = input(prompt).strip()
        try:
            number = float(value)
            if number <= 0:
                print("Value must be greater than zero.")
                continue
            return number
        except ValueError:
            print("Only numbers are allowed.")


dispenser = Dispenser()
attendant = FuelAttendant("MFDS Attendant", dispenser)

try:
    while True:
        display_menu()
        choice = get_menu_choice()

        try:
            if choice == "1":
                fuels = attendant.view_fuels()
                if not fuels:
                    print("No fuel available.")
                    continue
                for fuel in fuels:
                    print(
                        f"{fuel.name} | ₦{fuel.price_per_liter}/L | {fuel.quantity}L available"
                    )

            elif choice == "2":
                name = get_alpha_string("Fuel name: ")
                price = get_numeric_value("Price per liter: ")
                quantity = get_numeric_value("Initial quantity (liters): ")
                attendant.add_fuel(Fuel(name, price, quantity))
                print("Fuel added successfully.")

            elif choice == "3":
                name = get_alpha_string("Fuel name: ")
                try:
                    new_price = get_numeric_value("New price per liter: ")
                    attendant.update_fuel_price(name, new_price)
                    print("Fuel price updated.")
                except FuelNameNotFoundError:
                    print("Fuel not found.")


            elif choice == "4":
                name = get_alpha_string("Fuel name: ")
                try:
                    liters = get_numeric_value("Liters to restock: ")
                    attendant.restock_fuel(name, liters)
                    print("Fuel restocked successfully.")
                except FuelNameNotFoundError:
                    print("Fuel not found.")


            elif choice == "5":
                name = get_alpha_string("Fuel name: ")
                liters = get_numeric_value("Liters to buy (1–50): ")
                tranx = attendant.dispense_by_liters(name, liters)
                print("\n--- RECEIPT ---")
                print(tranx.receipt())

            elif choice == "6":
                name = get_alpha_string("Fuel name: ")
                amount = get_numeric_value("Amount to spend (₦): ")
                tranx = attendant.dispense_by_amount(name, amount)
                print("\n--- RECEIPT ---")
                print(tranx.receipt())

            elif choice == "7":
                transactions = attendant.transactions()
                if not transactions:
                    print("No transactions yet.")
                    continue
                for tranx in transactions:
                    print(tranx.receipt())

            elif choice == "0":
                print("System shutting down...")
                break

            else:
                print("Invalid option.")

        except InsufficientFuelQuantityError:
            print("Not enough fuel available.")
        except InvalidDispenseValueError:
            print("Invalid dispense value.")
        except FuelNameNotFoundError:
            print("Fuel not found.")

except KeyboardInterrupt:
    print("\nSystem terminated by user.")
