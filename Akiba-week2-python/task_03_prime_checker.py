num= int(input("Please enter the number : "))
if num <= 1:
     print (f"{num} is not a prime number.")
else:
    for i in range (2, num+1): # we add 1 to the num to handle that 2 is not a prime number.
        if num % i==0:
            print (f"{num} is not a prime number.")
            break # we don't need to check every divisors because if it's divisible by another number rather than one and itself,it is not a prime number.
            
        else :
            print (f"{num} is a prime number.")
