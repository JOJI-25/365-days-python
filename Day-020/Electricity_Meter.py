class ElectricityMeter:

  def __init__(self, house_number, previous_reading, current_reading):
    if previous_reading < 0 or current_reading < 0:
      raise ValueError("Readings cannot be negative.")
    if current_reading < previous_reading:
      raise ValueError("Current reading cannot be lower than previous reading.")

    self.house_number = house_number
    self.previous_reading = previous_reading
    self.current_reading = current_reading

  def add_reading(self, new_reading):
    if new_reading < 0:
      print("Error: Readings cannot be negative.")
      return
    if new_reading < self.current_reading:
      print("Error: New meter reading cannot be lower than the previous reading.")
      return

    self.previous_reading = self.current_reading
    self.current_reading = new_reading
    print(f"New reading {new_reading} added successfully.")

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

  def display_bill(self):
    units = self.get_units_used()
    bill = self.calculate_bill()
    print(f"House: {self.house_number}")
    print(f"Previous Reading: {self.previous_reading}")
    print(f"Current Reading: {self.current_reading}")
    print(f"Units Used: {units}")
    print(f"Bill: Rs. {bill}\n")



meter1 = ElectricityMeter("House 1", 100, 250)

meter1.display_bill()

meter1.add_reading(300)     
meter1.display_bill()

meter1.add_reading(350)
meter1.display_bill()   