check=[0]*1000005

def sieve(n):
    prime = [True for i in range(n+1)]
    p = 2

    while p*p<=n:
        if prime[p]==True:
             check[p]+=1
             for i in range(p*2,n+1,p):
                prime[i]=False

        p = p+1

    for i in range(2,n+1):
        if prime[i]:
            check[i]+=1
sieve(1000005)

n=int(input())
for i in range(n):
     x=int(input())
     if check[x]!=0:print('%d is a prime number.'%(x))
     else:print('%d is not a prime number.'%(x))
