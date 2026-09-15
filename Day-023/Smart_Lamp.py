class SmartLamp:
    def __init__(self,room_name):
        self.room = room_name
        self.is_on = False
    
    def turn_on(self):
        print("Turning On!!!")
        self.is_on = True
        print("The lamp is now ON")
    
    def turn_off(self):
        print("Turning Off...")
        self.is_on = False
        print("The lamp is now OFF")

    def display(self):
        print(f"The lamp in {self.room} is {'ON' if self.is_on else 'OFF'}")


smart_lamp = SmartLamp("Living Room")

smart_lamp.display()
smart_lamp.turn_on()
smart_lamp.turn_off()
smart_lamp.display()

