num_1 = float(input ("Please enter the first number : "))
num_2 = float (input ("Please enter the second number : "))
num_3 = float(input ("Please enter the third number : "))


if num_1 ==num_2 and num_1 == num_3:
    print ("The three numbers are equal.")
elif num_1 == num_2 and num_1!=num_3:
    if num_1 > num_3:
        print (f"The largest is {num_1}")
    else:
        print (f"The largest is {num_3}")
    print (f"{num_1} and {num_2} are equal.")
elif num_1 == num_3 and num_1!=num_2:
    if num_1 > num_2:
        print (f"The largest is {num_1}")
    else:
        print (f"The largest is {num_2}")
    print (f"{num_1} and {num_3} are equal.")
elif num_3== num_2 and num_1!=num_3:
    if num_3 > num_1:
        print (f"The largest is {num_3}")
    else:
        print (f"The largest is {num_1}")
    print (f"{num_3} and {num_2} are equal.")
else:
    if num_1> num_2:
        if num_1>num_3:
            print (f"{num_1} is the largest number.")
        else:
            print (f"{num_3} is the largest number.")
    else:
        if num_2 > num_3:
            print (f"{num_2} is the largest number.")
        else :
            print (f"{num_3} is the largest number ")