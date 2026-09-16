class TrafficSignal:
    def __init__(self,location,color):
        self.location = location
        self.color = color

    def change_color(self,new_color):
        if new_color == "Red" or "Yellow" or "Green":
            self.color = new_color
            print("Updated Color: ",self.color)
        else:
            print("Invalid")

    def display(self):
        print(f"Location: {self.location}")
        print(f"Color: {self.color}")

    
trafic1 = TrafficSignal("Busy Junction","Red")
trafic1.change_color("Green")
trafic1.display()

trafic2 = TrafficSignal("Main Road","Yellow")
trafic2.change_color("Red")
trafic2.display()

