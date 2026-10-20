#Create a program that asks the user to enter 10 numbers.
#The program should analyze the numbers and display:
#The largest number
#The smallest number
#The total sum
#The average
#How many numbers are even
#How many numbers are odd

sum = 0
even = 0
odd = 0
for i in range (1,11):
    number= int(input (f"Enter the number {i} : "))
    sum += number 
    if i==1:
        largest = number 
        smallest= number 
    if number> largest :
        largest= number 
    if number<smallest :
        smallest= number 
    if number %2 == 0:
        even+=1
    else:
        odd +=1
    average= sum /10
print ()
print ("=========================")
print ()
print (f"The largest number is {largest}")
print (f"The smallest number is {smallest}")
print (f"The total sum is {sum}")
print (f"There are {even} even numbers in it ")
print (f"There are {odd} odd numbers in it.")
print (f"The average of the numbers is {average}")

