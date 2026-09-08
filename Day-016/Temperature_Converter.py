class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9 / 5) + 32

    def to_kelvin(self):
        return self.celsius + 273.15

    def set_celsius(self, new_celsius):
        self.celsius = new_celsius

    def display(self):
        f_temp = self.to_fahrenheit()
        k_temp = self.to_kelvin()
        
        print(f"Celsius: {self.celsius}°C")
        print(f"Fahrenheit: {f_temp}°F")
        print(f"Kelvin: {k_temp}K")


temp = Temperature(25)
print("Initial Temperature:")
temp.display()

print("After changing Celsius to 0:")
temp.set_celsius(0)
temp.display()