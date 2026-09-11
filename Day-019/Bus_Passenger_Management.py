class Passenger:
    def __init__(self, name, passenger_id):
        self.name = name
        self.passenger_id = passenger_id

    def __str__(self):
        return f"[{self.passenger_id}] {self.name}"


class Bus:
    def __init__(self, bus_number, capacity):
        self.bus_number = bus_number
        self.capacity = capacity
        self.passengers = {} 

    def is_full(self):
        return len(self.passengers) >= self.capacity

    def available_seats(self):
        return self.capacity - len(self.passengers)

    def add_passenger(self, passenger):
        if self.is_full():
            print(f"Cannot board {passenger.name}. Bus {self.bus_number} is full.")
            return

        if passenger.passenger_id in self.passengers:
            print(f"Passenger ID {passenger.passenger_id} is already on the bus.")
            return

        self.passengers[passenger.passenger_id] = passenger
        print(f"Boarded: {passenger.name}. Seats left: {self.available_seats()}")

    def remove_passenger(self, passenger_id):
        if passenger_id not in self.passengers:
            print(f"Cannot remove. Passenger ID {passenger_id} is not on the bus.")
            return

        
        removed_passenger = self.passengers.pop(passenger_id)
        print(f"Alighted: {removed_passenger.name}. Seats left: {self.available_seats()}")

    def search_passenger(self, passenger_id):
        passenger = self.passengers.get(passenger_id)
        if passenger:
            print(f"Found: {passenger}")
            return passenger
        else:
            print(f"Passenger ID {passenger_id} not found.")
            return None

    def display_passengers(self):
        print(f"\n--- Passengers on Bus {self.bus_number} ---")
        if not self.passengers:
            print("The bus is currently empty.")
        else:
            for passenger in self.passengers.values():
                print(passenger)
        print("----------------------------------\n")



my_bus = Bus("KL-15-1234", 4)

p1 = Passenger("Alice", "P001")
p2 = Passenger("Bob", "P002")
p3 = Passenger("Charlie", "P003")
p4 = Passenger("Diana", "P004")
p5 = Passenger("Eve", "P005")

print("--- Boarding Initial Passengers ---")
my_bus.add_passenger(p1)
my_bus.add_passenger(p2)
my_bus.add_passenger(p3)

my_bus.display_passengers()

print("--- Testing Capacity ---")
my_bus.add_passenger(p4) 
my_bus.add_passenger(p5) 

print("\n--- Testing Duplicates ---")
my_bus.add_passenger(p1)

print("\n--- Testing Removal and Searching ---")
my_bus.search_passenger("P002")
my_bus.remove_passenger("P002")
my_bus.remove_passenger("P099")

print("\n--- Final State ---")
my_bus.add_passenger(p5)
my_bus.display_passengers()