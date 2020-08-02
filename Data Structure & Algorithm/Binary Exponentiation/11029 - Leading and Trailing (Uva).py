from math import log10

def power(a,b,m):
    result = 1
    a = a%m
    while b>0:
        if b%2==1:
            result = (result*a)%m
        a = (a*a) % m
        b = b//2

    return result%m



for I in range(int(input())):
    a,b = map(int,input().split())

    temp = log10(a)*b
    frac = temp - int(temp)
    first = int(pow(10,frac) * 100)
    last = ('000'+str(power(a,b,1000)))[-3:]

    print(str(first)+'...'+last)
