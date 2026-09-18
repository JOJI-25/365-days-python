class Elevator:
    def __init__(self,current_floor,max_floor,min_floor):
        self.current_floor = current_floor
        self.max_floor = max_floor
        self.min_floor = min_floor

    def go_to_floor(self,floor):
        if floor > self.max_floor:
            print("Error: Already at top floor!")
        elif floor < self.min_floor:
            print("Error: Already at bottom floor!")
        else:
            self.current_floor = floor
            print(f"Elevator moved to floor {self.current_floor}")

    def go_up(self,floors):
        for i in range(floors):
            if self.current_floor > self.max_floor:
                print("Error: Already at top floor!")
            else:
                self.current_floor += 1
                print(f"Elevator moved up to floor {self.current_floor}")

        if self.current_floor > self.min_floor:
            self.current_floor -= 1
            print(f"Elevator moved down to floor {self.current_floor}")
        else:
            print("Error: Already at bottom floor!")


    def go_down(self,floors):
        for i in range(floors):
            if self.current_floor < self.max_floor:
                self.current_floor -= 1
                print(f"Elevator moved down to floor {self.current_floor}")
            else:
                print("Error: Already at bottom floor!")

    
    def display_floors(self):
        print(f"Current Floor: {self.current_floor}")

elevator = Elevator(1,10,1)
elevator.go_to_floor(5)
elevator.go_to_floor(1)
elevator.go_to_floor(10)
elevator.go_up(5)
elevator.go_down(5)
elevator.display_floors()