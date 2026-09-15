class Employee:
    def __init__(self, name, employee_id, hours_worked=0):
        self.name = name
        self.employee_id = employee_id
        self.hours_worked = max(0, hours_worked)

    def add_hours(self, hours):
        if hours <= 0:
            print(f"Error for {self.name}: Hours added must be positive.")
            return
        self.hours_worked += hours

    def get_overtime_hours(self):
        if self.hours_worked > 40:
            return self.hours_worked - 40
        return 0

    def calculate_pay(self):
        regular_hours = min(self.hours_worked, 40)
        overtime_hours = self.get_overtime_hours()
        
        regular_pay = regular_hours * 500
        overtime_pay = overtime_hours * 750
        
        return regular_pay + overtime_pay

    def display_summary(self):
        regular_hours = min(self.hours_worked, 40)
        overtime_hours = self.get_overtime_hours()
        total_pay = self.calculate_pay()

        print(f"Employee: {self.name}")
        print(f"ID: {self.employee_id}")
        print(f"Total Hours Worked: {self.hours_worked}")
        print(f"Regular hours: {regular_hours}")
        print(f"Overtime hours: {overtime_hours}")
        print(f"Total pay: ₹{total_pay}\n")




emp1 = Employee("Arun", "E101")
emp2 = Employee("Divya", "E102")

emp1.add_hours(45)

emp2.add_hours(30)
emp2.add_hours(8) 

emp1.display_summary()
emp2.display_summary()