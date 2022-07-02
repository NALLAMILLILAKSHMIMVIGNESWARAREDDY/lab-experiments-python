'''Write a program that generates a list of 20 random numbers between 1 and 100. 
(a) Print the list. 
(b) Print the average of the elements in the list. 
(c) Print the largest and smallest values in the list. 
(d) Print the second largest and second smallest entries in the list 
(e) Print how many even numbers are in the list.'''
import random
l=random.sample(range(1, 100), 20)
print(*l)
print(sum(l)/20)
l.sort()
print(max(l),min(l))
print(l[-2],l[1])
print(len([i for i in l if i%2==0]))
