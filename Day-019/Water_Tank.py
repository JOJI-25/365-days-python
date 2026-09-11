class water_tank:
    def __init__(self,capacity,current_water_level):
        self.capacity = capacity

        if current_water_level > capacity:
            raise ValueError("current water level cannot be greater than capacity")

        elif current_water_level < 0:
            raise ValueError("current water level cannot be less than 0")

        self.current_water_level = current_water_level
        
    def fill(self,amount):
        if amount > self.capacity:
            raise ValueError("amount is greater than capacity")

        elif amount < 0:
            raise ValueError("amount is less than 0")
        self.current_water_level += amount


    def drain(self,amount):
        if self.capacity != 0 and amount > self.capacity:
            raise ValueError("amount is greater than capacity")

        elif self.capacity != 0 and amount < 0:
            raise ValueError("amount is less than 0")

        self.current_water_level -= amount

    def remaining_capacity(self):
        return self.capacity - self.current_water_level

    def display_status(self):
        print(f"Water level: {self.current_water_level}")
        print(f"Remaining capacity: {self.remaining_capacity()}")



tank1 = water_tank(100,50)
print("-"*10)
print("Adding Water")
tank1.fill(20)
print("-"*10)
tank1.display_status()
print("-"*10)
tank1.drain(30)
print("-"*10)
tank1.display_status()
print("-"*10)
        

        

        
