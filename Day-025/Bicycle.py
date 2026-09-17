class Bicycle:
    def __init__(self,brand,total_distance_ridden,current_speed):
        self.brand = brand
        if total_distance_ridden <0:
            raise ValueError("Invalid total distance")
        self.total_distance_ridden = total_distance_ridden

        if current_speed <0:
            raise ValueError("Invalid current speed")
        self.current_speed = current_speed


    def ride(self,distance):
        if distance <0:
            raise ValueError
        self.total_distance_ridden +=distance

    
        
    def set_speed(self,speed):
        if speed <0:
            raise ValueError
        self.current_speed = speed


    def stop(self):
        self.current_speed = 0


    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Speed: {self.current_speed}")
        print(f"Total Distance Ridden: {self.total_distance_ridden}")


cycle1 = Bicycle("Trek",10,20)
cycle1.display_info()  

print("\n")

cycle1.ride(15)
print("\n")

cycle1.display_info()


print("\n")

cycle1.set_speed(30)
print("\n")

cycle1.display_info()

print("\n")

cycle1.stop()
print("\n")

cycle1.display_info()  