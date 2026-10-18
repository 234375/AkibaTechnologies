word = input ("Enter the word : ")
word = word.lower()
reverse= ""
for letter in word :
    reverse= letter + reverse 
if word == reverse :
    print (f"{word} is a palindrome.")
else:
    print (f"{word} is not a palindrome.")