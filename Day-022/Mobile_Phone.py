class MobilePhone:
    def __init__(self,brand,model,battery=0):
        self.brand = brand
        self.model = model
        self.battery = battery

    def display_info(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Battery : {self.battery}")


    def charge(self):
        if self.battery >= 100:
            print("Battery is full")
        else:
            self.battery += 10
            print("Battery level is ", self.battery)


    def use_phone(self):
        if self.battery == 0:
            print("Battery is dead")
        else:
            self.battery -= 10
            print("Battery level : ", self.battery)

phone = MobilePhone("Samsung","S22")

phone.display_info()

phone.charge()

phone.use_phone()

phone.battery = 90

phone.charge()

phone.use_phone()