from math import sqrt,ceil

def sieve(n):
    prime = [True for i in range(n+1)]
    p = 2;dic={};a=[]

    while p*p<=n:
        if prime[p]==True:
            for i in range(p*2,n+1,p):
                prime[i]=False

        p = p+1

    for i in range(2,n+1):
        if prime[i]:
            dic[i]=1
    return dic

a=sieve(1000005)

y=int(input())
z=list(map(int,input().split()))

for i in z:
    n=sqrt(i)
    if n==ceil(n):
        try:
            if a[n]:
                print('YES')
        except KeyError:
            print('NO')
        
    else:
        print('NO')
    
