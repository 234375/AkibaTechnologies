number = int(input("Enter the number: "))
number = abs(number) # to handle -ve and +ve numbers
count = 0

while number > 0:
    digit = number % 10 # it takes the reminder because we use modulo operator.
    count += digit
    number = number // 10 # to remove the last digit and gives us integer number. so that the loop iterates effectively. without it the iteration doesn't work properly.

print(f"The total sum of the digits  is {count}")