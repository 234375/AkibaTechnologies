def validate_units(units):
    if units < 0:
        return False
    else:
        return True

def calculate_first_tier(units):
    if units > 50:
        return 50 * 0.50
    else:
        return units * 0.50

def calculate_second_tier(units):
    if units > 50:
        if units >= 150:
            return 100 * 0.75
        else:
            return (units - 50) * 0.75
    else:
        return 0

def calculate_third_tier(units):
    if units > 150:
        return (units - 150) * 1.20
    else:
        return 0

def calculate_total_bill(units, service_fee=0):
    first_charge = calculate_first_tier(units)
    second_charge = calculate_second_tier(units)
    third_charge = calculate_third_tier(units)
    total = first_charge + second_charge + third_charge + service_fee
    return total

def generate_summary(units, service_fee=0):
    first_charge = calculate_first_tier(units)
    second_charge = calculate_second_tier(units)
    third_charge = calculate_third_tier(units)
    total = calculate_total_bill(units, service_fee)
    print("\n========== ELECTRICITY BILL ==========")
    print("Units consumed:", units)
    print("First 50 units:", first_charge, "Birr")
    print("Next 100 units:", second_charge, "Birr")
    print("Above 150 units:", third_charge, "Birr")
    print("Service fee:", service_fee, "Birr")
    print("--------------------------------------")
    print("Total bill:", total, "Birr") print("======================================")

units = float(input("Enter electricity units consumed: "))
if validate_units(units):
    service_fee = float(input("Enter service fee (0 if none): "))
    if service_fee < 0:
        print("Service fee cannot be negative.")
    else:
        generate_summary(units, service_fee)
else:
    print("Invalid units! Units cannot be negative.")