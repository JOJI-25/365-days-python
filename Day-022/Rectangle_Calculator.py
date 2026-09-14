class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def display(self):
        print("Length : ", self.length)
        print("Breadth : ", self.breadth)
        print("Area : ", self.area())
        print("Perimeter : ", self.perimeter())


rectangle1 = Rectangle(10, 20)
rectangle1.display()

rectangle1.length = 15

print("\nAfter updating length:")
rectangle1.display()