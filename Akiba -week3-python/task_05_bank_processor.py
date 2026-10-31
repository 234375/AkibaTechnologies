balance = 1000
transactions = []
daily_limit = 2000
withdrawn_today = 0

def deposit_money(amount):
    global balance
    if amount <= 0:
        return "Error: Deposit amount must be positive."
    balance += amount
    record_transaction("deposit", amount)
    return f"Deposit successful! New balance: {balance} Birr"


def withdraw_money(amount):
    global balance, withdrawn_today
    if amount <= 0:
        return "Error: Withdrawal amount must be positive."
    if amount > balance:
        return "Error: Insufficient balance."
    if withdrawn_today + amount > daily_limit:
        return "Error: Daily withdrawal limit exceeded."
    balance -= amount
    withdrawn_today += amount
    record_transaction("withdrawal", amount)
    return f"Withdrawal successful! New balance: {balance} Birr"


def check_balance():
    return balance


def record_transaction(transaction_type, amount):
    transaction = {
        "type": transaction_type,
        "amount": amount,
        "balance_after": balance
    }
    transactions.append(transaction)


def generate_summary():
    total_deposited = 0
    total_withdrawn = 0
    for transaction in transactions:
        if transaction["type"] == "deposit":
            total_deposited += transaction["amount"]
        elif transaction["type"] == "withdrawal":
            total_withdrawn += transaction["amount"]
    print("\n===== BANK ACCOUNT SUMMARY =====")
    print(f"Opening balance: 1000 Birr")
    print(f"Total deposited: {total_deposited} Birr")
    print(f"Total withdrawn: {total_withdrawn} Birr")
    print(f"Final balance: {check_balance()} Birr")
    print("\nTransaction History:")
    if len(transactions) == 0:
        print("No successful transactions.")
    else:
        for transaction in transactions:
            print(transaction)

while True:
    print("\n===== BANK MENU =====")
    print("1. Deposit money")
    print("2. Withdraw money")
    print("3. Check balance")
    print("4. Transaction summary")
    print("5. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        print(deposit_money(amount))
    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        print(withdraw_money(amount))
    elif choice == "3":
        print(f"Current balance: {check_balance()} Birr")
    elif choice == "4":
        generate_summary()
    elif choice == "5":
        print("Thank you for using our bank!")
        generate_summary()
        break
    else:
        print("Invalid choice. Please try again.")