customer_name = input("Enter customer name: ")
product = input("Enter product name: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print()
print("========================================")
print("              RECEIPT")
print("========================================")

print(f"Customer: {customer_name}")
print ()
print (f"product       price        quantity")
print (".........................................")
print(f" {product}       {price}            {quantity}")
print ()
print(f"Total:   {total:.2f} ETB")

print()
print("Thank you for shopping!")
print("========================================")