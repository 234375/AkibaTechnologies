correct_pin = 1234
attempts = 3

while attempts > 0:
    PIN = int(input("Please enter the correct PIN: "))

    if PIN != correct_pin:
        print("Incorrect PIN.")
        attempts -= 1
        print(f"Attempts remaining: {attempts}")
    else:
        print("Login successful.")
        break # we use break because if the pin is correct,the program should stop the execution. without it even if the correct pin, the execution iterates.
