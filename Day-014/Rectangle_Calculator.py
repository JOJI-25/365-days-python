class rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)        
    def display(self):
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")


length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

rect = rectangle(length,width)


rect.display()