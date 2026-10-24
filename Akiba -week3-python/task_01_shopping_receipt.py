def calculate_subtotal(items):
    subtotal = 0
    for item in items:
        subtotal += item["price"] * item["quantity"]
    return subtotal


def calculate_discount(subtotal):#calculate discount 
    if subtotal >= 3000:
        return subtotal * 0.10
    elif subtotal >= 1000:
        return subtotal * 0.05
    return 0


def calculate_tax(amount, tax_rate):
    return amount * tax_rate


def generate_receipt(items, tax_rate):
    if tax_rate < 0 or tax_rate > 1:
        print("Invalid tax rate!")
        return

    for item in items:
        if item["price"] < 0 or item["quantity"] < 0:
            print("Invalid price or quantity!")
            return

    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal)
    amount = subtotal - discount
    tax = calculate_tax(amount, tax_rate)
    total = amount + tax

    print("--- SHOPPING RECEIPT ---")
    print ()
    for item in items:
        print(f'{item["name"]}: {item["price"]} x {item["quantity"]}')

    print(f"Subtotal: {subtotal:.2f} Birr")
    print(f"Discount: {discount:.2f} Birr")
    print(f"Tax: {tax:.2f} Birr")
    print(f"Final Amount: {total:.2f} Birr")


items = [
    {"name": "Notebook", "price": 80, "quantity": 3},
    {"name": "Pen", "price": 15, "quantity": 5}
]

generate_receipt(items, 0.15)