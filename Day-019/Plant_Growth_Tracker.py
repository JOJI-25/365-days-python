class plant:
    def __init__(self, name,height_cm):
        self.name = name
        self.height_cm = height_cm

    def grow(self,amount):
        self.height_cm += amount

    def trim(self,amount):
        self.height_cm -= amount

    def get_height(self):
        return self.height_cm

    def display(self):
        print(f"Plant Name: {self.name}")
        print(f"Plant Height: {self.height_cm}")

plant1 = plant("rose", 12)
plant1.display()

plant1.grow(5)
plant1.display()

plant1.trim(2)
plant1.display()
