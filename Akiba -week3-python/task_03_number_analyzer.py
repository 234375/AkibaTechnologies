def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def get_divisors(number):
    divisors = []
    if number == 0:
        return divisors
    number = abs(number)
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors


def sum_of_digits(number):
    number = abs(number)
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number = number // 10
    return total


def reverse_number(number):
    if number <0:
        sign =-1
    else :
        sign= 1
    number = abs(number)
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit #we multiply by 10 because when we reverse the digit increase from ones place to tenth place.
        number = number // 10
    return reversed_number * sign


def analyze_number(number):
    print("\n===== NUMBER ANALYSIS =====")
    print("Number:", number)
    if number % 2 == 0:
        print("Type: Even")
    else:
        print("Type: Odd")
    print("Is Prime:", is_prime(number))
    print("Sum of Digits:", sum_of_digits(number))
    print("Reversed Number:", reverse_number(number))
    print("Positive Divisors:", get_divisors(number))


number = int(input("Enter an integer: "))
analyze_number(number)