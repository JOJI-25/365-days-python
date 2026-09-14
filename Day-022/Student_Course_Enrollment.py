class Course:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __str__(self):
        return f"{self.name} ({self.code})"


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.enrolled_courses = []

    def enroll(self, course):
        if course in self.enrolled_courses:
            print(f"Note: {self.name} is already enrolled in {course.name}.")
        else:
            self.enrolled_courses.append(course)
            print(f"{self.name} successfully enrolled in {course.name}.")

    def view_courses(self):
        print(f"\nCourses enrolled by {self.name} ({self.student_id}):")
        if not self.enrolled_courses:
            print("  - No courses enrolled.")
        for course in self.enrolled_courses:
            print(f"  - {course}")



student1 = Student("Aarav", "STU001")
course1 = Course("Math", "MATH101")
course2 = Course("Science", "SCI101")

student1.enroll(course1)
student1.enroll(course2)
student1.view_courses()

