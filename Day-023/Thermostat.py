class Thermostat:
    def __init__(self, room_name, temperature=20):
        self.room_name = room_name
        self.temperature = max(10, min(35, temperature))

    def increase_temperature(self, amount):
        if amount <= 0:
            print("Error: Amount to increase must be positive.")
            return
        
        new_temp = self.temperature + amount
        if new_temp > 35:
            self.temperature = 35
            print(f"Temperature capped at maximum limit of 35°C.")
        else:
            self.temperature = new_temp

    def decrease_temperature(self, amount):
        if amount <= 0:
            print("Error: Amount to decrease must be positive.")
            return
        
        new_temp = self.temperature - amount
        if new_temp < 10:
            self.temperature = 10
            print(f"Temperature capped at minimum limit of 10°C.")
        else:
            self.temperature = new_temp

    def display_temperature(self):
        print(f"Room: {self.room_name}")
        print(f"Temperature: {self.temperature}°C\n")



living_room = Thermostat("Living Room", 24)
bedroom = Thermostat("Bedroom", 18)

living_room.display_temperature()

print("Increase Living Room by 4°C")
living_room.increase_temperature(4)
living_room.display_temperature()

print("Decrease Living Room by 10°C")
living_room.decrease_temperature(10)
living_room.display_temperature()

print("--- Bedroom Test ---")
bedroom.display_temperature()

print("Decrease Bedroom by 15°C (Should hit minimum 10°C limit)")
bedroom.decrease_temperature(15)
bedroom.display_temperature()