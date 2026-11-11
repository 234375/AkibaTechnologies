#================================
# Task 2: Rectangle Calculator
#================================

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)

rectangle1 = Rectangle(10, 5)
rectangle2 = Rectangle(8, 4)

print("Rectangle 1")
print ()
print("Length:", rectangle1.length)
print("Width:", rectangle1.width)
print("Area:", rectangle1.area())
print("Perimeter:", rectangle1.perimeter())

print("------------------------")
print ()
print("Rectangle 2")
print ()
print("Length:", rectangle2.length)
print("Width:", rectangle2.width)
print("Area:", rectangle2.area())
print("Perimeter:", rectangle2.perimeter())