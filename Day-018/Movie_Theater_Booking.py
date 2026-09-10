class Seat:
  def __init__(self, seat_number, price):
    self.seat_number = seat_number
    self.price = price
    self.is_available = True


class Booking:
  def __init__(self, customer_name, seat, amount_paid):
    self.customer_name = customer_name
    self.seat = seat
    self.amount_paid = amount_paid


class Theater:
  def __init__(self, name):
    self.name = name
    self.seats = {}  
    self.bookings = {}  
    
  def add_seat(self, seat_number, price):
    self.seats[seat_number] = Seat(seat_number, price)

  def display_seats(self):
    print(f"\n--- {self.name} Seat Status ---")
    for seat_number, seat in self.seats.items():
      status = "Available" if seat.is_available else "Booked"
      print(f"{seat_number} -> Rs.{seat.price} -> {status}")

  def book_seat(self, seat_number, customer_name):
    if seat_number not in self.seats:
      print(f"Error: Seat {seat_number} does not exist.")
      return

    seat = self.seats[seat_number]
    if not seat.is_available:
      print(f"Error: Seat {seat_number} is already booked.")
      return

    seat.is_available = False
    new_booking = Booking(customer_name, seat, seat.price)
    self.bookings[seat_number] = new_booking
    print(f"Success: {customer_name} booked seat {seat_number}.")

  def cancel_booking(self, seat_number):
    if seat_number not in self.seats:
      print(f"Error: Seat {seat_number} does not exist.")
      return

    if seat_number not in self.bookings:
      print(f"Error: Seat {seat_number} is not currently booked.")
      return

    seat = self.seats[seat_number]
    seat.is_available = True
    del self.bookings[seat_number]
    print(f"Success: Booking for seat {seat_number} has been canceled.")

  def calculate_revenue(self):
    total = 0
    for booking in self.bookings.values():
      total += booking.amount_paid
    return total

my_theater = Theater("Grand Cinema")
my_theater.add_seat("A1", 150)
my_theater.add_seat("A2", 150)
my_theater.add_seat("B1", 200)
my_theater.add_seat("B2", 200)
my_theater.add_seat("C1", 250)


my_theater.display_seats()

print("\n--- Booking Phase ---")
my_theater.book_seat("B1", "Rahul")
my_theater.book_seat("C1", "Anu")

my_theater.display_seats()
print(f"Current Revenue: Rs.{my_theater.calculate_revenue()}")

print("\n--- Cancellation Phase ---")
my_theater.cancel_booking("B1")

my_theater.display_seats()
print(f"Current Revenue: Rs.{my_theater.calculate_revenue()}")