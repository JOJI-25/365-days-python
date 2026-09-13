class InventoryItem:
    def __init__(self,item_code,name,price,stock):
        self.item_code = item_code
        self.name = name
        self.price = price
        self.stock = stock

    def add_stocks(self,quantity):
        if quantity > 0:
            self.stock += quantity
        else:
            print("Error")

    def sell(self,quantity):
        if quantity > 0 and self.stock != 0:
            self.stock -= quantity
            print("Sold")
        else:
            print("Error")

    def get_stock_value(self):
        return self.stock * self.price

    def is_available(self):
        if self.stock > 0:
            return True
        else:
            return False


    def display(self):
        print("Item Code: ",self.item_code)
        print("Name: ",self.name)
        print("Price: ",self.price)
        print("Stock: ",self.stock)
        print("Stock Value: ",self.get_stock_value())


my_item = InventoryItem(item_code="123456789",name="Mouse",price=100,stock=10)
my_item.display()

my_item.add_stocks(10)
my_item.display()

my_item.sell(5)
my_item.display()


    