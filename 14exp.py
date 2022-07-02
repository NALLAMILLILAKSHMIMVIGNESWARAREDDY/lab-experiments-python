'''Write a program that generates 100 random integers that are either 0 or 1. Then
find the longest run of zeros, the largest number of zeros in a row. For instance, the 
longest run of zeros in [1,0,1,1,0,0,0,0,1,0,0] is '''
import random
l=[]
for i in range(100):
 n=random.randint(0,1)
 l.append(n)
maxx=0
c=0
print(*l)
for i in range(100):
 if l[i]==0:
 c+=1
 maxx=max(c,maxx)
 else:
 c=0
print(maxx)
