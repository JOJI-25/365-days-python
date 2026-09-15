class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class VendingMachine:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        print("Available Products:")
        for index, product in enumerate(self.products, 1):
            print(f"{index}. {product.name}   ₹{product.price}   Quantity: {product.quantity}")
        print()

    def find_product(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None

    def purchase_product(self, product_name, money_inserted):
        product = self.find_product(product_name)
        if not product:
            print(f"Error: '{product_name}' is not available in the machine.\n")
            return

        if product.quantity <= 0:
            print(f"Purchase failed: {product.name} is out of stock.\n")
            return

        if money_inserted < product.price:
            shortage = product.price - money_inserted
            print(f"Purchase failed: Insufficient money. {product.name} costs ₹{product.price}. You inserted ₹{money_inserted} (Short by ₹{shortage}).\n")
            return

        change = money_inserted - product.price
        product.quantity -= 1 

        print("Purchase successful!")
        print(f"Change returned: ₹{change}")
        print(f"Remaining {product.name}: {product.quantity}\n")


machine = VendingMachine()

machine.add_product(Product("Water", 20, 5))
machine.add_product(Product("Juice", 40, 3))
machine.add_product(Product("Chips", 30, 4))

machine.display_products()

print("--- Transaction ---")
print("Select: Juice")
print("Inserted: ₹50")
machine.purchase_product("Juice", 50)
machine.display_products()