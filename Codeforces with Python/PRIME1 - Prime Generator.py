n=1000000000
prime = [True for i in range(n+1)]

for i in range(n+1):
    if i%2==0:
        prime[i]=False
    else:
        prime[i]=True

p = 2

'''
while p*p<=n:
    if prime[p]==True:
         for i in range(p*2,n+1,p):
               prime[i]=False
    p = p+1
'''
