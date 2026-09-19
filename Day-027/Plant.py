class Plant:
    def __init__(self, name, height, age_days):
        self.name = name
        self.height = max(0.0, float(height))
        self.age_days = max(0, int(age_days))

    def increase_height(self, amount):
        self.height = max(0.0, self.height + amount)

    def grow(self, days):
        if days <= 0:
            print(f"Error: Days to grow must be positive. ({days} provided)")
            return
        
        self.age_days += days
        growth_amount = days * 2
        self.increase_height(growth_amount)

    def display_info(self):
        print(f"Plant: {self.name}")
        print(f"Height: {self.height} cm")
        print(f"Age: {self.age_days} days\n")


rose = Plant("Rose", 20, 10)
sunflower = Plant("Sunflower", 40, 15)
fern = Plant("Fern", 10, 5)

print("--- Initial Plant States ---")
rose.display_info()
sunflower.display_info()
fern.display_info()



print("--- Growing Rose by 5 days ---")
rose.grow(5)
rose.display_info()

print("--- Growing Sunflower by 10 days ---")
sunflower.grow(10)
sunflower.display_info()

print("--- Growing Fern by 3 days ---")
fern.grow(3)
fern.display_info()