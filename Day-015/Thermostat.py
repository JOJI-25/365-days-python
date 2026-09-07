class Thermostat:
    def __init__(self, room_name, temperature):
        self.room_name = room_name
        self.temperature = temperature

    def increase_temperature(self, amount):
        self.temperature += amount
        print(f"Increasing by {amount} degree celsius")
        print(f"Temperature: {self.temperature}")

    def decrease_temperature(self, amount):
        self.temperature -= amount
        print(f"Decreasing by {amount} degree celsius")
        print(f"Temperature: {self.temperature}")

    def display_temperature(self):
        print(f"Current temperature in {self.room_name}: {self.temperature}°C")


if __name__ == "__main__":
    room_name = input("Enter the Room Name: ")
    temperature = float(input("Enter the Temperature: "))

    # Instance variable uses lower_snake_case while class uses PascalCase
    my_thermostat = Thermostat(room_name, temperature)

    my_thermostat.display_temperature()
    print()
    my_thermostat.increase_temperature(5)
    print()
    my_thermostat.decrease_temperature(2)
    print()
    my_thermostat.display_temperature()