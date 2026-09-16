class ElectricityMeter:
    def __init__(self, house_number, previous_reading=0, current_reading=0):
        if previous_reading < 0 or current_reading < 0:
            raise ValueError("Readings cannot be negative.")
        if current_reading < previous_reading:
            raise ValueError("Current reading cannot be lower than previous reading.")
        
        self.house_number = house_number
        self.previous_reading = previous_reading
        self.current_reading = current_reading

    def add_reading(self, reading):
        if reading < 0:
            raise ValueError("Readings cannot be negative.")
        if reading < self.current_reading:
            raise ValueError("The new meter reading cannot be lower than the previous reading.")
        
        self.previous_reading = self.current_reading
        self.current_reading = reading

    def get_units_used(self):
        return self.current_reading - self.previous_reading

    def calculate_bill(self):
        units = self.get_units_used()
        bill = 0

        if units <= 100:
            bill = units * 2
        elif units <= 200:
            bill = (100 * 2) + ((units - 100) * 3)
        else:
            bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)

        return bill

    def display_summary(self):
        units = self.get_units_used()
        bill = self.calculate_bill()
        print(f"--- Electricity Meter Summary ---")
        print(f"House Number     : {self.house_number}")
        print(f"Previous Reading : {self.previous_reading}")
        print(f"Current Reading  : {self.current_reading}")
        print(f"Units Consumed   : {units}")
        print(f"Total Bill       : ₹{bill}\n")

house1 = ElectricityMeter("House-12", previous_reading=100, current_reading=350)
house1.display_summary()

house2 = ElectricityMeter("House-45", previous_reading=500, current_reading=500)
house2.add_reading(680)
house2.display_summary()