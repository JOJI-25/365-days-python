class TrafficSignal:
    def __init__(self,location,color="Red"):
        self.location = location
        self.color = color

    def change_to_green(self, color):
        if color in ("Green", "green", "GREEN", "G"):
            self.color = "Green"
            return "This color is now green"
        else:
            return "This color is not green"
        
    def change_to_yellow(self, color):
        if color in ("Yellow", "yellow", "YELLOW", "Y"):
            self.color = "Yellow"
            return "This color is now yellow"
        else:
            return "This color is not yellow"
        
    def change_to_red(self, color):
        if color in ("Red", "red", "RED", "R"):
            self.color = "Red"
            return "This color is now red"
        else:
            return "This color is not red"


    def display(self):
        print(f"Location: {self.location}")
        print(f"Signal: {self.color}")


signal1 = TrafficSignal("mg road","green")
signal1.change_to_green("green")
signal1.display()
signal1.change_to_yellow("yellow")
signal1.display()
signal1.change_to_red("red")
signal1.display()

