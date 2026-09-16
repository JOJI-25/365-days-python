class WaterBottle:
    def __init__(self,capacity,current_water):
        self.capacity = capacity
        self.current_water = current_water

    def fill(self,amount):
        if amount > 0:
            new_water = self.current_water + amount
            if new_water > self.capacity:
                print("Bottle cannot hold more water")
            else:
                self.current_water = new_water
                print("Filled with ",new_water)
        else:
            print("Enter a valid amount")

    def drink(self,amount):
        if amount > 0:
            new_water = self.current_water - amount
            if new_water < 0:
                print("Not enough water in the bottle")
            else:
                self.current_water = new_water
                print("Drank ",new_water)
        else:
            print("Enter a valid amount")

    def get_remaining_capacity(self):
        return self.capacity - self.current_water

    def display(self):
        print("Capacity: ",self.capacity)
        print("Current water: ",self.current_water)
        print("Remaining capacity: ",self.get_remaining_capacity())



bottle = WaterBottle(2000,500)
print("Initial state:")
bottle.display()
print("--------------------------")
print("Filling the bottle with 1000ml:")
bottle.fill(1000)
print("--------------------------")
print("Drinking 1500ml from the bottle:")
bottle.drink(1500)
print("--------------------------")
bottle.display()