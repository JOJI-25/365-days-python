class Fan:
    def __init__(self,brand,speed = 0,is_on = "OFF"):
        self.brand = brand
        self.speed = speed
        self.is_on = is_on

    def turn_on(self):
        print("Turning on!!!")
        self.is_on = "ON"
        self.speed = 0
        print(f"Status: {self.is_on}")
        print(f"Speed: {self.speed}")

    def turn_of(self):
        print("Turning of!!!")
        self.is_on = "OFF"
        self.speed = 0
        print(f"Status: {self.is_on}")
        print(f"Speed: {self.speed}")

    def increasing_speed(self):
        print("Increasing speed!!")
        if 0<=self.speed<5:
            self.speed+=1
            print(f"Speed: {self.speed}")

    def dcreaming_speed(self):
        print("Decreaming speed!!")
        if 1 <= self.speed <= 5:
            self.speed -= 1
            print(f"Speed: {self.speed}")

    def show_status(self):
        print("Showing Status")
        print(f"Brand: {self.brand}")
        print(f"Status: {self.is_on}")
        print(f"Speed: {self.speed}")


my_fan = Fan(brand="Bajaj")
my_fan.show_status()
my_fan.turn_on()
my_fan.increasing_speed()
my_fan.increasing_speed()
my_fan.increasing_speed()
my_fan.dcreaming_speed()
my_fan.show_status()
my_fan.turn_of()