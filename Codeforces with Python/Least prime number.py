def sieve(n):
    prime = [True for i in range(n+1)]
    p = 2

    while p*p<=n:
        if prime[p]==True:
            for i in range(p*2,n+1,p):
                prime[i]=False

        p = p+1

    for i in range(2,n+1):
        if prime[i]:
            prime[i]=i

    return prime

#Unfinished
