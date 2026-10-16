name = input ("Enter your name : ")
python_score = float(input("Enter your python score: "))
English_score = float(input("Enter your English score: "))
mathematics_score = float(input("Enter your mathematics score: "))

total = python_score + English_score + mathematics_score
average = total/3

print ("===========================")
print ("      STUDENT RESULT     ")
print ("===========================")
print ()
print (f" Student : {name}")
print ()
print (f"Python:               {python_score}")
print (f"English:               {English_score}")
print (f"Mathematics:               {mathematics_score}")
print ("----------------------------------------------")
print ()
print (f"Average:            {average:.2f}")
print ("=======================")