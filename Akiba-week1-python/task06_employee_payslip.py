employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
transport_allowance = float(input("Enter transport allowance: "))
food_allowance = float(input("Enter food allowance: "))

gross_salary = basic_salary + transport_allowance + food_allowance

print()
print("========================================")
print("          EMPLOYEE PAYSLIP")
print("========================================")

print(f"Employee: {employee_name}")
print()
print(f"Basic Salary:           {basic_salary:.2f} ETB")
print(f"Transport Allowance:    {transport_allowance:.2f} ETB")
print(f"Food Allowance:         {food_allowance:.2f} ETB")
print("----------------------------------------")
print(f"Gross Salary:            {gross_salary:.2f}ETB")

print("========================================")