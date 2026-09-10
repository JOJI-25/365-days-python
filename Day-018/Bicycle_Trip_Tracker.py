class bicycle:
    def __init__(self,brand,total_distance,current_speed):
        self.brand = brand
        self.total_distance = total_distance
        self.current_speed = current_speed

    def ride(self,distance):
        self.total_distance += distance
        return f"Current distance: {self.total_distance} km"

    def set_speed(self,speed):
        self.current_speed = speed
        return f"Current speed: {self.current_speed} km/h"

    def stop(self):
        self.current_speed = 0
        return f"Current speed: {self.current_speed} km/h"

    def get_distance(self):
        return self.total_distance

    def display_status(self):
        print(f"Brand Name : {self.brand}")
        print(f"Total distance: {self.total_distance} Km")
        print(f"Current speed : {self.current_speed} Km/h")

my_bike = bicycle(brand = "hero",total_distance = 0,current_speed = 0)
my_bike.display_status()
my_bike.ride(20)
my_bike.set_speed(30)
my_bike.display_status()
my_bike.stop()
my_bike.display_status()

print(my_bike.get_distance())