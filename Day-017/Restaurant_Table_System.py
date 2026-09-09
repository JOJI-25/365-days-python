class Table:
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.is_occupied = False

    def can_accommodate(self, group_size):
        return not self.is_occupied and self.capacity >= group_size

    def occupy(self):
        self.is_occupied = True

    def release(self):
        if not self.is_occupied:
            return False
        self.is_occupied = False
        return True


class Restaurant:
    def __init__(self):
        self.tables = []

    def add_table(self, table_number, capacity):
        new_table = Table(table_number, capacity)
        self.tables.append(new_table)

    def display_tables(self):
        print("--- Current Restaurant Status ---")
        for table in self.tables:
            status = "Occupied" if table.is_occupied else "Available"
            print(f"Table {table.table_number} -> Capacity: {table.capacity} -> {status}")
        print(f"Total Available Tables: {self.count_available_tables()}\n")

    def count_available_tables(self):
        return sum(1 for table in self.tables if not table.is_occupied)

    def assign_table(self, group_size):
        suitable_tables = [t for t in self.tables if t.can_accommodate(group_size)]
        
        if not suitable_tables:
            print(f"Sorry, no suitable table available for a group of {group_size}.\n")
            return None
            
        best_table = min(suitable_tables, key=lambda t: t.capacity)
        
        best_table.occupy()
        print(f"Group of {group_size} assigned to Table {best_table.table_number}.\n")
        return best_table

    def release_table(self, table_number):
        for table in self.tables:
            if table.table_number == table_number:
                success = table.release()
                if success:
                    print(f"Table {table_number} has been released and is now available.\n")
                else:
                    print(f"Table {table_number} is already available.\n")
                return
        
        print(f"Error: Table {table_number} does not exist.\n")

my_restaurant = Restaurant()
my_restaurant.add_table(1, 2)
my_restaurant.add_table(2, 4)
my_restaurant.add_table(3, 6)
my_restaurant.add_table(4, 4)

my_restaurant.tables[3].occupy()

print("INITIAL STATE:")
my_restaurant.display_tables()

print("A group of 3 arrives...")
my_restaurant.assign_table(3)

print("AFTER ASSIGNMENT:")
my_restaurant.display_tables()

print("The group leaves Table 2...")
my_restaurant.release_table(2)

print("FINAL STATE:")
my_restaurant.display_tables()

print("TESTING EDGE CASES:")
my_restaurant.release_table(1) 
my_restaurant.assign_table(10) 