products = []

def add_product(products, name, price, stock):
    if name.strip() == "":
        print("Product name cannot be empty.")
        return
    if search_product(products, name) is not None:
        print("Product already exists.")
        return
    if price < 0:
        print("Price cannot be negative.")
        return
    if stock < 0:
        print("Stock cannot be negative.")
        return
    product = {
        "name": name,
        "price": price,
        "stock": stock
    }
    products.append(product)
    print("Product added successfully.")


def search_product(products, name):
    for product in products:
        if product["name"].lower() == name.lower():
            return product
    return None


def update_price(products, name, new_price):
    product = search_product(products, name)
    if product is None:
        print("Product not found.")
        return
    if new_price < 0:
        print("Price cannot be negative.")
        return
    product["price"] = new_price
    print("Price updated successfully.")


def increase_stock(products, name, quantity):
    product = search_product(products, name)
    if product is None:
        print("Product not found.")
        return
    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return
    product["stock"] += quantity
    print("Stock increased successfully.")


def sell_product(products, name, quantity):
    product = search_product(products, name)
    if product is None:
        print("Product not found.")
        return
    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return
    if quantity > product["stock"]:
        print("Not enough stock available.")
        return
    product["stock"] -= quantity
    print("Product sold successfully.")


def calculate_inventory_value(products):
    total_value = 0
    for product in products:
        value = product["price"] * product["stock"]
        total_value += value
    return total_value


def low_stock_report(products, threshold=5):
    print("\nLOW STOCK REPORT")
    found = False
    for product in products:
        if product["stock"] < threshold:
            print(
                product["name"],
                "- Remaining stock:",
                product["stock"]
            )
            found = True
    if not found:
        print("No low-stock products found.")


while True:
    print("\n===== INVENTORY STOCK CONTROLLER =====")
    print("1. Add Product")
    print("2. Search Product")
    print("3. Update Product Price")
    print("4. Increase Stock")
    print("5. Sell Product")
    print("6. Calculate Inventory Value")
    print("7. Low Stock Report")
    print("8. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        stock = int(input("Enter stock quantity: "))
        add_product(products, name, price, stock)
    elif choice == "2":
        name = input("Enter product name: ")
        product = search_product(products, name)
        if product is not None:
            print("Product:", product)
        else:
            print("Product not found.")
    elif choice == "3":
        name = input("Enter product name: ")
        new_price = float(input("Enter new price: "))
        update_price(products, name, new_price)
    elif choice == "4":
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity to add: "))
        increase_stock(products, name, quantity)
    elif choice == "5":
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity to sell: "))
        sell_product(products, name, quantity)
    elif choice == "6":
        total = calculate_inventory_value(products)
        print("Total inventory value:", total, "Birr")
    elif choice == "7":
        threshold = int(input("Enter low-stock threshold (default 5): "))
        low_stock_report(products, threshold)
    elif choice == "8":
        print("Thank you for using the Inventory System!")
        break
    else:
        print("Invalid choice. Please try again.")