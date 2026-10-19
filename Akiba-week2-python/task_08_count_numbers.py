#Ask the user for a positive number N.Your program should count from 1 to N and calculate:
#How many numbers are even
#How many numbers are odd
#The sum of all numbers
#Computational Thinking Challenge
#Do not solve each result separately.


number = int(input ("Enter positive number: "))
even = 0
odd = 0
sum =0
for i in range (1, number+1):
    sum +=i
    if i %2==0:
        even += 1
    else :
       odd += 1
print (f"There are {odd} odd numbers in it.")
print (f"There are {even} even numbers in it.")
print (f"The sum is {sum}")
     
     
     