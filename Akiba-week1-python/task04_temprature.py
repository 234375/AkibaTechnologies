celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

fahrenheit_formula= (celsius * 9 / 5) + 32
celsius_formula = (fahrenheit - 32) * 5 / 9
print()
print("===========================")
print(" TEMPERATURE")
print("===========================")
print(f"Celsius: {celsius:.2f}°C")
print(f"Fahrenheit: {fahrenheit_formula:.2f}°F")
print()
print(f"Fahrenheit: {fahrenheit:.2f}°F")
print(f"Celsius: {celsius_formula:.2f}°C")
print("===========================")