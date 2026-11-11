from abc import ABC, abstractmethod
import math

class Dog:
    def make_sound(self):
        print("Dog: Woof!")
class Cat:
    def make_sound(self):
        print("Cat: Meow!")
class Cow:
    def make_sound(self):
        print("Cow: Moo!")

dog = Dog()
cat = Cat()
cow = Cow()
animals = [dog, cat, cow]
print("POLYMORPHISM")

for animal in animals:
    animal.make_sound()

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi * self.radius ** 2

rectangle = Rectangle(10, 5)
circle = Circle(7)
print("\nABSTRACTION")
print("Rectangle Area:", rectangle.calculate_area())
print("Circle Area:", round(circle.calculate_area(), 2))