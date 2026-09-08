class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class VendingMachine:
    def __init__(self):
        self.inventory = {}
        self.inserted_money = 0

    def add_product(self, code, product):
        self.inventory[code] = product

    def display_products(self):
        print("--- Available Products ---")
        for code, product in self.inventory.items():
            status = f"Quantity: {product.quantity}" if product.quantity > 0 else "OUT OF STOCK"
            print(f"{code} - {product.name.ljust(10)} ₹{product.price} - {status}")
        print("-" * 26)

    def insert_money(self, amount):
        if amount > 0:
            self.inserted_money += amount
            print(f"Inserted: ₹{amount}. Total balance: ₹{self.inserted_money}")
        else:
            print("Please insert a valid amount.")

    def cancel_transaction(self):
        if self.inserted_money > 0:
            print(f"Transaction cancelled. Refunded: ₹{self.inserted_money}\n")
            self.inserted_money = 0
        else:
            print("No money to refund.\n")

    def purchase(self, code):
        print(f"\nAttempting to purchase: {code}")
        
        if code not in self.inventory:
            print("Invalid selection.")
            self.cancel_transaction()
            return

        product = self.inventory[code]

        if product.quantity == 0:
            print(f"{product.name} is currently out of stock.")
            self.cancel_transaction()
            return
        if self.inserted_money < product.price:
            print(f"Insufficient funds. {product.name} costs ₹{product.price}.")
            self.cancel_transaction()
            return

        product.quantity -= 1
        change = self.inserted_money - product.price
        
        self.inserted_money = 0 

        print(f"Product: {product.name}")
        print(f"Price: ₹{product.price}")
        print(f"Money Inserted: ₹{product.price + change}")
        print(f"Change: ₹{change}")
        print("Purchase successful")
        print(f"Remaining Quantity: {product.quantity}\n")


machine = VendingMachine()

machine.add_product("A1", Product("Cola", 40, 3))
machine.add_product("A2", Product("Chips", 25, 5))
machine.add_product("A3", Product("Chocolate", 30, 2))

machine.display_products()

machine.insert_money(50)
machine.purchase("A1")
machine.insert_money(10)
machine.purchase("A2")

machine.insert_money(100)
machine.purchase("A3")
machine.insert_money(100)
machine.purchase("A3")
machine.insert_money(50)
machine.purchase("A3")