def primes(num=100):
    i=1
    n=2
    L=[]
    while i<=num:
        l=1
        count=0
        while l<=n:
            x=n%l
            if x==0:
                count=count+1
            l=l+1
        if count==2:
            L.append(n)
            i=i+1
        n=n+1
    return L
num=int(input("enter a number"))
print(primes())
        
