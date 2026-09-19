class Table:
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.is_occupied = False 

    def assign(self):
        self.is_occupied = True

    def release(self):
        self.is_occupied = False

    def display_info(self):
        status = "Occupied" if self.is_occupied else "Available"
        print(f"Table {self.table_number} -> Capacity: {self.capacity} -> {status}")


class Restaurant:
    def __init__(self):
        self.tables = {}  

    def add_table(self, table_number, capacity):
        if table_number in self.tables:
            print(f"Error: Table {table_number} already exists.")
            return
        self.tables[table_number] = Table(table_number, capacity)

    def display_all_tables(self):
        for table in self.tables.values():
            table.display_info()
        print(f"Available tables: {self.count_available_tables()}\n")

    def find_available_table(self, num_people):
        suitable_tables = [
            t for t in self.tables.values() 
            if not t.is_occupied and t.capacity >= num_people
        ]
        
        if not suitable_tables:
            return None
        
        suitable_tables.sort(key=lambda x: x.capacity)
        return suitable_tables[0]

    def assign_table(self, num_people):
        table = self.find_available_table(num_people)
        if table:
            table.assign()
            print(f"Table {table.table_number} assigned for {num_people} people.\n")
            return table.table_number
        else:
            print(f"Sorry, no available table found for {num_people} people.\n")
            return None

    def release_table(self, table_number):
        if table_number in self.tables:
            self.tables[table_number].release()
            print(f"Table {table_number} has been released and is now available.\n")
        else:
            print(f"Error: Table {table_number} does not exist.")

    def count_available_tables(self):
        return sum(1 for t in self.tables.values() if not t.is_occupied)



my_restaurant = Restaurant()
my_restaurant.add_table(1, 2)
my_restaurant.add_table(2, 4)
my_restaurant.add_table(3, 6)

print("--- Initial Restaurant State ---")
my_restaurant.display_all_tables()


my_restaurant.assign_table(4)

print("--- Restaurant State After Assignment ---")
my_restaurant.display_all_tables()