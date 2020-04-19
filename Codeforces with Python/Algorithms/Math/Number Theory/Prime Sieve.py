n=500000000
from math import sqrt as s

prime=[True for i in range (n+1)]
p=2

while p*p<=n:
    if prime[p]==True:
        for i in range (p*2,n+1,p):
            prime[i]=False
        
    p+=1

a=[];count=0
for p in range(2,n+1):
    if prime[p]:
        a.append(p)
        count+=1


#O(n*log(logn))
