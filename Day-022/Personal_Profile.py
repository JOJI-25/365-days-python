class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")




person1 = Person("Anu",21)
person2 = Person("Rahul",22)

person1.display()
print("")
person2.display()