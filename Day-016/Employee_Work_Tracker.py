class Employee:
    def __init__(self, name, employee_id, hours_worked=0):
        self.name = name
        self.employee_id = employee_id
        self.hours_worked = hours_worked

    def add_hours(self, hours):
        self.hours_worked += hours

    def calculate_overtime(self):
        if self.hours_worked > 40:
            return self.hours_worked - 40
        else:
            return 0

    def calculate_regular_pay(self):
        if self.hours_worked > 40:
            return 40 * 500
        else:
            return self.hours_worked * 500

    def display_summary(self):
        overtime_hours = self.calculate_overtime()
        regular_hours = self.hours_worked - overtime_hours
        
        regular_pay = self.calculate_regular_pay()
        overtime_pay = overtime_hours * 750
        total_pay = regular_pay + overtime_pay

        print(f"Employee: {self.name}")
        print(f"ID: {self.employee_id}")
        print(f"Hours Worked: {self.hours_worked}\n")
        
        print(f"Regular Hours: {regular_hours}")
        print(f"Overtime Hours: {overtime_hours}")
        print(f"Regular Pay: ₹{regular_pay}")
        print(f"Overtime Pay: ₹{overtime_pay}")
        print(f"Total Pay: ₹{total_pay}")
        print("-" * 30)

emp1 = Employee("Aisha", "E101")
emp1.add_hours(40)
emp1.display_summary()

emp2 = Employee("Ravi", "E102")
emp2.add_hours(46)
emp2.display_summary()

emp3 = Employee("Karan", "E103", 30) 
emp3.display_summary()