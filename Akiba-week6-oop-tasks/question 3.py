# Question 3: Inheritance and Method Overriding
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print("Employee Information")
        print("Name:", self.name)
        print("Salary:", self.salary, "Birr")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    def display_info(self):
        print("Manager Information")
        print("Name:", self.name)
        print("Salary:", self.salary, "Birr")
        print("Department:", self.department)
        print("------------------------")
        
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_info(self):
        print("Developer Information")
        print("Name:", self.name)
        print("Salary:", self.salary, "Birr")
        print("Programming Language:", self.programming_language)
        print("------------------------")

employee1 = Manager("Ahmed", 25000, "Human Resources")
employee2 = Developer("Sara", 30000, "Python")

employee1.display_info()
employee2.display_info()