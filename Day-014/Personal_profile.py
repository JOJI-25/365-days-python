class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f"name:{self.name}")
        print(f"age:{self.age}")
        

person1 = person("joji",22)

person1.display()