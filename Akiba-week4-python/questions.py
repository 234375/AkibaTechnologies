#Question 1: Mutable and Immutable Objects
#Explain the difference between mutable and immutable objects in Python.
#Write a Python program that demonstrates the difference between modifying a list and modifying a string. Explain the output

Mutable objects: Objects whose values can be changed after creation. Example: Lists (list).
Immutable objects: Objects whose values cannot be changed after creation. Example: Strings (str).

# Modifying a list (mutable)
numbers = [10, 20, 30]
numbers[0] = 100
print(numbers)
#output
[100, 20, 30]

# Modifying a string (immutable)
name = "Python"
name = name + " Programming"
print(name)
#output 
Python Programming 

The list is mutable, so we can change its elements directly.
The string is immutable, so we cannot change its original characters. Instead, Python creates a new string.


#Question 2: References and Object Identity
#Study the following code:
#a = [10, 20, 30]
#b = a
#c = [10, 20, 30]
#print(a is b)
#print(a is c)
#print(a == c)
#What is the output?
True
False
True
#Explain the difference between is and ==
is checks whether two variables refer to the same object in memory.
== checks whether two objects have the same values.
a and b have the same identity because b = a makes both variables refer to the same list.

#Why do a and c have the same values but different identities?
a and c have different identities because they are two separately created lists, even though their values are the same.

#Question 3: Shared References and Side Effects
#Consider the following code:
#numbers = [1, 2, 3]
#values = numbers
#values.append(4)
#print(numbers)
#print(values)
#Predict the output.
[1, 2, 3, 4]
[1, 2, 3, 4]
#Explain why modifying values also affects numbers.
values = numbers makes both variables refer to the same list in memory.
append(4) modifies the original list.
Therefore, the change appears in both variables.
#Rewrite the code so that modifying values does not change numbers.
numbers = [1, 2, 3]
values = numbers.copy()
values.append(4)
print(numbers)
print(values)
#output
[1, 2, 3]
[1, 2, 3, 4]
copy() creates a separate list. Therefore, modifying values does not affect numbers.

#Question 4: Function Arguments and Mutability
#def update_list(items):
   # items.append(100)
#scores = [50, 60, 70]
#update_list(scores)
#print(scores)
#What is the output?
[50, 60, 70, 100]
#Explain why the original list changes after the function call.
The list scores is passed to the function.
The parameter items refers to the same list as scores.
Since lists are mutable, items.append(100) changes the original list.
#Modify the function so that it creates and returns a new list without changing the original list
def update_list(items):
    new_list = items.copy()
    new_list.append(100)
    return new_list
scores = [50, 60, 70]
updated_scores = update_list(scores)
print(scores)
print(updated_scores)
#output
[50, 60, 70]
[50, 60, 70, 100]
The function creates a copy of the original list and modifies the copy. Therefore, the original list remains unchanged.


#Question 5: Memory Management and Garbage Collection

#Explain how Python manages objects in memory and how garbage collection works.
Python manages objects in memory automatically. It uses reference counting and garbage collection to identify and remove objects that are no longer needed, freeing up memory.
#Write a Python program that creates a list, assigns it to another variable, and then removes one reference using del.
# Creating a list
numbers = [10, 20, 30]
# Assigning the same list to another variable
values = numbers
# Removing one reference
del numbers
print(values)
#output
[10, 20, 30]
#What happens when del is used?
del removes a variable reference, but does not necessarily destroy the object.
#Does deleting one variable always destroy the object?
No. If another variable refers to the same object, it remains accessible.
#What happens when an object is no longer referenced?
Python identifies it as unused and can reclaim its memory through garbage collection.

