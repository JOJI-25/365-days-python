class studentresult:
    def __init__(self,student_name,student_id,mark1,mark2,mark3):
        if not (0 <= mark1 <= 100 and 0 <= mark2 <= 100 and 0 <= mark3 <= 100):
            raise ValueError("Marks must be between 0 and 100")
        self.student_name = student_name
        self.student_id = student_id
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def total_marks(self):
        return self.mark1 + self.mark2 + self.mark3

    def average_marks(self):
        return self.total_marks() // 3

    def get_grade(self):
        if 90 <= self.average_marks() <= 100:
            return "A"
        elif 80 <= self.average_marks() <= 89:
            return "B"
        elif 70 <= self.average_marks() <= 79:
            return "C"
        elif 60 <= self.average_marks() <= 69:
            return "D"
        else:
            return "F"

    def display(self):
        print(f"Student Name : {self.student_name}")
        print(f"Student ID : {self.student_id}")
        print(f"Total Marks : {self.total_marks()}")
        print(f"Average Marks : {self.average_marks()}")
        print(f"Grade : {self.get_grade()}")


student1 = studentresult("Anu", "S101", 85, 78, 92)
student2 = studentresult("Rahul", "S102", 95, 91, 88)
student3 = studentresult("Priya", "S103", 65, 58, 70)

student1.display()
student2.display()
student3.display()
