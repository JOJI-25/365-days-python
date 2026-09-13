class Student:
    def __init__(self, student_id, name, assigned_stop):
        self.student_id = student_id
        self.name = name
        self.assigned_stop = assigned_stop

class BusRoute:
    def __init__(self):
        self.stops = []
        self.students = {} 
        self.stop_directory = {} 

    def add_stop(self, stop_name):
        if stop_name not in self.stops:
            self.stops.append(stop_name)
            self.stop_directory[stop_name] = []

    def register_student(self, student_id, name, stop_name):
        if stop_name not in self.stops:
            print(f"Error: Stop '{stop_name}' does not exist.")
            return
        if student_id in self.students:
            print(f"Error: Student '{student_id}' is already registered.")
            return
        
        new_student = Student(student_id, name, stop_name)
        self.students[student_id] = new_student
        self.stop_directory[stop_name].append(new_student)

    def find_student(self, student_id):
        if student_id in self.students:
            s = self.students[student_id]
            return s.name, s.assigned_stop
        return "Student not found"

    def get_total_students(self):
        return len(self.students)

student1 = Student("123456789", "Aarav", "1st Stop")
student2 = Student("987654321", "Vihaan", "2nd Stop")

my_route = BusRoute()
my_route.add_stop("1st Stop")
my_route.add_stop("2nd Stop")
my_route.register_student(student1.student_id, student1.name, student1.assigned_stop)
my_route.register_student(student2.student_id, student2.name, student2.assigned_stop)
print("Total Students:", my_route.get_total_students())  


