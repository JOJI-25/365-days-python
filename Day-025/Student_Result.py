class StudentResult:
    def __init__(self, student_name, student_id, marks):
        self.student_name = student_name
        self.student_id = student_id
        
        for subject, mark in marks.items():
            if not (0 <= mark <= 100):
                raise ValueError(f"Mark for {subject} must be between 0 and 100.")
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks.values())

    def calculate_average(self):
        total = self.calculate_total()
        return total / len(self.marks)

    def get_grade(self):
        avg = self.calculate_average()
        
        if 90 <= avg <= 100:
            return "A"
        elif 80 <= avg <= 89:
            return "B"
        elif 70 <= avg <= 79:
            return "C"
        elif 60 <= avg <= 69:
            return "D"
        elif 50 <= avg <= 59:
            return "E"
        else:
            return "F"

    def display_result(self):
        print(f"Student: {self.student_name}")
        print(f"ID: {self.student_id}\n")
        print("Marks:")
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")
        print(f"\nTotal: {self.calculate_total()}")
        print(f"Average: {self.calculate_average():.2f}")
        print(f"Grade: {self.get_grade()}")
        print("-" * 30)


student1 = StudentResult(
    student_name="Rahul", 
    student_id="S101", 
    marks={"Python": 85, "Maths": 78, "Physics": 92}
)

student2 = StudentResult(
    student_name="Ananya", 
    student_id="S102", 
    marks={"Python": 95, "Maths": 91, "Physics": 94}
)

student3 = StudentResult(
    student_name="Kiran", 
    student_id="S103", 
    marks={"Python": 45, "Maths": 55, "Physics": 50}
)


student1.display_result()
student2.display_result()
student3.display_result()