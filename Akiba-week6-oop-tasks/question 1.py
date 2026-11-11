# Question 1: Classes, Objects, Constructors,
# and Methods

class Student:
    def __init__(self, name, student_id, department):
        self.name = name
        self.student_id = student_id
        self.department = department
    def display_info(self):
        print("Student Information")
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Department:", self.department)
        print("---------------------------")
    def introduce(self):
        print(f"Hello! My name is {self.name}.")
        print(f"I am studying {self.department}.")
        print("---------------------------")

student1 = Student("Ahmed", "IT001", "Information Technology")
student2 = Student("Sara", "IT002", "Information Technology")
student3 = Student("Musa", "IT003", "Information Technology")

print("STUDENT INFORMATION")
student1.display_info()
student2.display_info()
student3.display_info()

print("\nSTUDENT INTRODUCTIONS")
student1.introduce()
student2.introduce()
student3.introduce()