class Seat:
    def __init__(self, seat_number, price):
        self.seat_number = seat_number
        self.price = price
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Booked"
        return f"{self.seat_number} -> ₹{self.price} -> {status}"


class Booking:
    def __init__(self, customer_name, seat):
        self.customer_name = customer_name
        self.seat = seat
        self.is_paid = False  


class Theater:
    def __init__(self):
        self.seats = {}
        self.bookings = {}

    def add_seat(self, seat_number, price):
        self.seats[seat_number] = Seat(seat_number, price)

    def view_available_seats(self):
        print("\n--- Available Seats ---")
        for seat in self.seats.values():
            print(seat)

    def check_seat_availability(self, seat_number):
        if seat_number not in self.seats:
            raise ValueError(f"Seat {seat_number} does not exist.")
        return self.seats[seat_number].is_available

    def book_seat(self, customer_name, seat_number):
        if seat_number not in self.seats:
            print(f"Error: Invalid seat number '{seat_number}'.")
            return None

        seat = self.seats[seat_number]
        if not seat.is_available:
            print(f"Error: Seat {seat_number} is already booked.")
            return None

        seat.is_available = False
        new_booking = Booking(customer_name, seat)
        self.bookings[seat_number] = new_booking
        print(f"Success: {customer_name} booked seat {seat_number}.")
        return new_booking

    def mark_booking_as_paid(self, seat_number):
        if seat_number in self.bookings:
            self.bookings[seat_number].is_paid = True
            print(f"Payment received for seat {seat_number}.")
        else:
            print(f"Error: No active booking found for seat {seat_number}.")

    def cancel_booking(self, seat_number):
        if seat_number in self.bookings:
            booking = self.bookings[seat_number]
            booking.seat.is_available = True
            del self.bookings[seat_number]
            print(f"Booking for seat {seat_number} has been cancelled.")
        else:
            print(f"Error: No active booking found for seat {seat_number}.")

    def calculate_total_revenue(self):
        total = sum(booking.seat.price for booking in self.bookings.values() if booking.is_paid)
        return total


theater = Theater()
theater.add_seat("A1", 150)
theater.add_seat("A2", 150)
theater.add_seat("B1", 250)
theater.add_seat("B2", 250)

theater.view_available_seats()

b1 = theater.book_seat("Rahul", "A1")
b2 = theater.book_seat("Anu", "B1")

theater.mark_booking_as_paid("A1")
theater.mark_booking_as_paid("B1")

theater.view_available_seats()

print(f"\nCurrent revenue: ₹{theater.calculate_total_revenue()}")

theater.cancel_booking("A1")

theater.view_available_seats()

print(f"\nCurrent revenue: ₹{theater.calculate_total_revenue()}")