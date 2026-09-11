class Room:
    def __init__(self, name, current_temperature):
        self.name = name
        self.current_temperature = max(10, min(35, current_temperature))

class Thermostat:
    def __init__(self, room, target_temperature):
        self.room = room
        self.target_temperature = 10 
        self.set_target_temperature(target_temperature)

    def set_target_temperature(self, temp):
        if temp < 10:
            self.target_temperature = 10
            print("Target adjusted to minimum limit: 10°C")
        elif temp > 35:
            self.target_temperature = 35
            print("Target adjusted to maximum limit: 35°C")
        else:
            self.target_temperature = temp
            print(f"Target set to {self.target_temperature}°C")

    def increase_temperature(self, amount=1):
        new_temp = self.room.current_temperature + amount
        
        if new_temp > 35:
            self.room.current_temperature = 35
            print(f"Cannot exceed 35°C. {self.room.name} is now 35°C.")
        else:
            self.room.current_temperature = new_temp
            print(f"Increased by {amount}°C. {self.room.name} is now {self.room.current_temperature}°C.")

    def decrease_temperature(self, amount=1):
        new_temp = self.room.current_temperature - amount
        
        if new_temp < 10:
            self.room.current_temperature = 10
            print(f"Cannot go below 10°C. {self.room.name} is now 10°C.")
        else:
            self.room.current_temperature = new_temp
            print(f"Decreased by {amount}°C. {self.room.name} is now {self.room.current_temperature}°C.")

    def check_status(self):
        print(f"\n--- {self.room.name} Thermostat ---")
        print(f"Current Temperature: {self.room.current_temperature}°C")
        print(f"Target Temperature: {self.target_temperature}°C")
        
        if self.room.current_temperature < self.target_temperature:
            print("Status: Heating Required")
        elif self.room.current_temperature > self.target_temperature:
            print("Status: Cooling Required")
        else:
            print("Status: Target Reached")


living_room = Room("Living Room", 24)

thermostat = Thermostat(living_room, 26)
thermostat.check_status()


thermostat.increase_temperature(2)

thermostat.check_status()

print("\n--- Testing Minimum Limits ---")
thermostat.decrease_temperature(20)