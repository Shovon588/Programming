def gameOn(a,b):
    b = bin(b)
    b = b[2:]
    print(b)
    result=1
    for i in range(len(b)):
        if b[i]=='0':
            result=(result*result)
        else:
            result=(result*result*a)
        return result


t=int(input())
from math import log10
mod=1000000000000037

for i in range(t):
    a,b,c=map(int,input().split())

    if a==0:print(0)
    elif b==0:print(1)
    elif c==0:print(a%mod)
    elif a==1:print(1)
    elif b==1:print(a%mod)
    elif c==1:
        temp=b*log10(a)
        temp=pow(10,temp)
        print(temp)

    else:
        temp=gameOn(b,c)
        
        result=gameOn(a,temp)
        result=result%mod

        print(result)
