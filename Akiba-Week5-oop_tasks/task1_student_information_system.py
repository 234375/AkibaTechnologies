#================================
# Task 1: Student Information System
# ===============================
class Student:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
    def display_info(self):
        print("Student Information")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.department)
        print("------------------------")

student1 = Student("Ahmed", 22, "Information Technology")
student2 = Student("Sara", 21, "Software Engineering")
student3 = Student("Musa", 23, "Computer science")

student1.display_info()
student2.display_info()
student3.display_info()