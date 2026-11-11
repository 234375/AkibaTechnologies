#================================
# Task 4: Product Information System
#================================
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def __str__(self):
        return f"Product: {self.name}, Price: {self.price} Birr, Quantity: {self.quantity}"
    def total_value(self):
        return self.price * self.quantity

product1 = Product("Laptop", 50000, 2)
product2 = Product("Mouse", 500, 10)
product3 = Product("Keyboard", 1200, 5)

print("PRODUCT INFORMATION")
print(product1)
print(product2)
print(product3)

print("\nTOTAL PRODUCT VALUES")
print(product1.name, "Total Value:", product1.total_value(), "Birr")

print(product2.name, "Total Value:", product2.total_value(), "Birr")

print(product3.name, "Total Value:", product3.total_value(), "Birr")