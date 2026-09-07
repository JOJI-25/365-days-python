class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        if price <= 0:
            raise ValueError("Price must be greater than 0.")
        self.price = price
        
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity

    def increase_quantity(self, amount):
        """Adds to the current quantity."""
        if amount > 0:
            self.quantity += amount

    def decrease_quantity(self, amount):
        """Subtracts from the current quantity safely."""
        if amount > 0:
            if self.quantity - amount < 0:
                print(f"Error: Cannot remove {amount}. Not enough in stock.")
            else:
                self.quantity -= amount

    def get_total_value(self):
        return self.price * self.quantity


my_item = Product(name="Wireless Mouse", price=800, quantity=2)

print(f"Product: {my_item.name}")
print(f"Price: ₹{my_item.price}")
print(f"Quantity: {my_item.quantity}")
print(f"Total: ₹{my_item.get_total_value()}")
print("-" * 20)

print("Adding 3 more...")
my_item.increase_quantity(3)

print(f"Quantity: {my_item.quantity}")
print(f"Total: ₹{my_item.get_total_value()}")