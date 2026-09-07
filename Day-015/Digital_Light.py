class Light:
    def __init__(self, roomName):
        self.roomName = roomName
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print("Turning on.....")

    def turn_off(self):
        self.is_on = False
        print("Turning off....")

    def status(self):
        if self.is_on:
            state = "ON"
        else:
            state = "OFF"

        print(f"{self.roomName} Light: {state}")


print("Light testing!!")

living_room_light = Light("Living Room")

living_room_light.status()
print()
living_room_light.turn_on()
living_room_light.status()
print()
living_room_light.turn_off()
living_room_light.status()
print()


print("--- Testing Two Different Lights ---")

kitchen_light = Light("Kitchen")


living_room_light.turn_on()

living_room_light.status()
kitchen_light.status()
