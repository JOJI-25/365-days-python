brand = input("Enter the brand name: ")
model = input("Enter the model name: ")
battery = int(input("Enter the battery percentage: "))





class Mobilephone:
    def __init__(self,brand,model,battery):
        self.brand = brand
        self.model = model
        self.battery = max(0, min(100,battery))

    def display_info(self):
        print(f"brand:{self.brand}")
        print(f"model: {self.model}")
        print(f"battery : {self.battery}")


    def charge(self):
        print("\nCharging!!!")
        self.battery = min(100, self.battery + 10)
        print(f"Battery : {self.battery}%")

    def use(self):
        print("\nUsing Phone!!")
        self.battery = max(0, self.battery - 10)
        print(f"Battery : {self.battery}%")
    
phone = Mobilephone(brand,model,battery)
phone.display_info()
phone.charge()
phone.use()  