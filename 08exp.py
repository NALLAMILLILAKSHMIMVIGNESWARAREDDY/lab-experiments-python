'''Write a program that asks the user to enter a word and prints out whether that word 
contains any vowels.'''
name=input("Enter Your Name")
count=0
l=['a','e','i','o','u']
for i in name:
    if i in l:
        count=1
        break
if(count==0):
    print("No vowels")
else:
    print("Vowels")
