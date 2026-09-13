class ParkingTicket:
    def __init__(self,ticket_id,vehicle_number,hours_parked):
        self.ticket_id = ticket_id
        self.vehicle_number = vehicle_number
        self.hours_parked = hours_parked

    def add_hours(self,hours):
        if hours > 0:
            self.hours_parked += hours
        else:
            print("Invalid hours")

    def calculate_fee(self):
       if self.hours_parked in (1, 2):
          return "50 Rupees"
       elif self.hours_parked == 3:
        return "70 Rupees"
       elif self.hours_parked == 4:
          return "90 Rupees"
       elif self.hours_parked == 5:
          return "110 Rupees"
       else:
          print("Error: Invalid hours")


    def display(self):
        print("Ticket ID:", self.ticket_id)
        print("Vehicle Number:", self.vehicle_number)
        print("Hours Parked:", self.hours_parked)
        print("Fee:", self.calculate_fee())

my_ticket = ParkingTicket(ticket_id="123456789", vehicle_number="HR26AB1234", hours_parked=2)
my_ticket.display()

my_ticket.add_hours(3)
my_ticket.display()
