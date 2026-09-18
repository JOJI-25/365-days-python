class TravelPass:
    def __init__(self,passenger,pass_id,remaining_trips):
        self.passenger = passenger
        self.pass_id = pass_id
        self.remaining_trips = remaining_trips

    def use_trip(self):
        if self.remaining_trips > 0:
            self.remaining_trips -= 1
            print("Trip used successfully!")
        else:
            print("Error: Not enough trips!")

    def add_trip(self,amount):
        if amount > 0:
            self.remaining_trips += amount
        else:
            print("Error: Invalid amount!")


    def check_trip(self):
        if self.remaining_trips > 0:
            print("Valid Pass!")
        else:
            print("Invalid Pass!")

    def display_pass(self):
        print(f"Passenger: {self.passenger}")
        print(f"Pass ID: {self.pass_id}")
        print(f"Remaining Trips: {self.remaining_trips}")

pass1 = TravelPass("John",12345,10)
pass1.display_pass()
pass1.check_trip()
pass1.use_trip()
pass1.display_pass()
pass1.add_trip(5)
pass1.display_pass()
pass1.check_trip()