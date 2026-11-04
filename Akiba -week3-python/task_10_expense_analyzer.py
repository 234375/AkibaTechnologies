expenses = [
    {"description": "Lunch", "category": "Food", "amount": 180},
    {"description": "Taxi", "category": "Transport", "amount": 120},
    {"description": "Groceries", "category": "Food", "amount": 450},
    {"description": "Internet", "category": "Bills", "amount": 300}
]

def add_expense(expenses, description, category, amount):
    if description == "" or category == "":
        print("Description and category cannot be empty.")
        return
    if amount <= 0:
        print("Amount must be greater than zero.")
        return
    new_expense = {
        "description": description,
        "category": category,
        "amount": amount
    }
    expenses.append(new_expense)
    print("Expense added successfully!")

def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


def spending_by_category(expenses):
    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
    return category_totals


def find_largest_expense(expenses):
    if len(expenses) == 0:
        return None
    largest = expenses[0]
    for expense in expenses:
        if expense["amount"] > largest["amount"]:
            largest = expense
    return largest

def find_expenses_above_threshold(expenses, threshold):
    result = []
    for expense in expenses:
        if expense["amount"] > threshold:
            result.append(expense)
    return result

def calculate_category_percentages(expenses):
    total = calculate_total(expenses)
    category_totals = spending_by_category(expenses)
    percentages = {}
    if total == 0:
        return percentages
    for category in category_totals:
        amount = category_totals[category]
        percentage = (amount / total) * 100
        percentages[category] = percentage
    return percentages

def highest_spending_category(expenses):
    category_totals = spending_by_category(expenses)
    if len(category_totals) == 0:
        return None
    highest_category = max(
        category_totals,
        key=category_totals.get
    )
    return highest_category

def generate_report(expenses, threshold):
    print("\n========== EXPENSE REPORT ==========")
    total = calculate_total(expenses)
    print("\nTotal Expenses:", total, "Birr")
    print("\nSpending By Category:")
    category_totals = spending_by_category(expenses)
    for category, amount in category_totals.items