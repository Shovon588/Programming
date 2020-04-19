import math

t=int(input())
def primeFact(n):
    a=[]
    while n%2==0:
        a.append(2)
        n=int(n/2)

    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i==0:
            a.append(i)
            n=int(n/i)


    if n>2:
        a.append(n)

    return a

while t>0:
    x=int(input())

    b=primeFact(x)

    print(max(b))

    t=t-1
