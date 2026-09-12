class WaterBottle:
    def __init__(self,capacity,current_level):
        self.capacity = capacity
        self.current_level = current_level

    def fill(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif self.current_level + amount > self.capacity:
            print(f"Only {self.capacity - self.current_level}ml can be added. Rest will overflow.")
        else:
            self.current_level += amount
            print(f"{amount}ml added. Current level: {self.current_level}ml")

    def drink(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount <= self.current_level:
            self.current_level -= amount
            print(f"{amount}ml drunk. Current level: {self.current_level}ml")
        else:
            print("Not enough water to drink.")

    def remaining_capacity(self):
        return self.capacity - self.current_level

    def current_water(self):
        return self.current_level

    def get_status(self):
        print(f"Capacity: {self.capacity}ml")
        print(f"Current level: {self.current_level}ml")
        print(f"Status: {'Full' if self.current_level == self.capacity else 'Not full'}")



water_bottle = WaterBottle(capacity=500, current_level=0)
water_bottle.fill(200)
water_bottle.drink(100)
print(water_bottle.current_water())
print(water_bottle.remaining_capacity())
water_bottle.get_status()