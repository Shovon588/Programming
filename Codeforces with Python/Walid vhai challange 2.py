n=10000

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
lena=count

while(1):
    n=int(input())
    if n==0:
        break

    j=0;b=[];count=0
    while(1):
        if j<lena and a[j]<=n:
            b.append(a[j])
            j+=1
        else:
            break
    
    for i in range(len(b)):
        sum=0
        for j in range(i,len(b)):
            sum+=b[j]

            if sum==n:
                count+=1
                break
            elif sum>n:
                break
    print(count)
