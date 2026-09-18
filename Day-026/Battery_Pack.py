class BatteryPack:
    def __init__(self,capacity,charge_level):
        if 1000 <=capacity <= 20000:
            self.capacity = capacity
        else:
            print("Invalid capacity!")
            self.capacity = 0
            
        if 0 <= charge_level <= 100:
            self.charge_level = charge_level
        else:
            print("Invalid charge level!")
            self.charge_level = 0    

    def charge(self,amount):
        if amount > 0:
            if self.charge_level + amount > self.capacity:
                print("Error: Battery will be overcharged!")
            else:
                self.charge_level += amount

    def use(self,amount):
        if amount > 0:
            if self.charge_level - amount < 0:
                print("Error: Not enough charge!")
            else:
                self.charge_level -= amount

    def display(self):
        print(f"Capacity: {self.capacity}")
        print(f"Charge Level: {self.charge_level}")

battery = BatteryPack(10000,5000)
battery.display()
battery.charge(2000)
battery.display()
battery.use(3000)
battery.display()
battery.charge(8000)
battery.display()
battery.use(12000)
battery.display()