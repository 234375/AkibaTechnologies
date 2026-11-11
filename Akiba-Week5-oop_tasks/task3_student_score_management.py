# ===============================
# Task 3: Student Score Management
#================================
class Student:
    school_name = "Akiba Academy"
    def __init__(self, name, score, department):
        self.name = name
        self.score = score
        self.department = department
    def display(self):
        print("Student Information")
        print("School:", self.school_name)
        print("Name:", self.name)
        print("Score:", self.score)
        print("Department:", self.department)
        print("------------------------")

student1 = Student("Ahmed", 85, "Information Technology")
student2 = Student("Sara", 90, "Software Engineering")
student3 = Student("Musa", 75, "Computer science")

print("BEFORE UPDATING SCORES")
print ()

student1.display()
student2.display()
student3.display()

student1.score = 95

print ()
print("AFTER UPDATING AHMED'S SCORE")
print ()

student1.display()
student2.display()
student3.display()