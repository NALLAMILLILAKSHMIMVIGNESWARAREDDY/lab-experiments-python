'''Write a program that asks the user for an integer and creates a list that consists of the 
factors of that integer.'''
n=int(input())
l=[]
for i in range(1,n+1):
 if n%i == 0:
 l.append(i)
print(*l)
