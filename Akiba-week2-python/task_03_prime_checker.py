#Write a program that determines whether a number is a prime number.A prime number is a number greater than 1 that can only be divided exactly by 1 and itself.
#Requirements.
#Your solution must use a loop to check possible divisors.
#Important Cases
#Your program should correctly handle:
#0 → Not Prime.  1 → Not Prime. 2 → Prime
#Challenge     Explain in your code comments why you do not need to check every number up to the input number.

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
