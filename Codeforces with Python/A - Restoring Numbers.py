from math import gcd
s,g = map(int,input().split())

temp=0;

if g%2==0 and s%2!=0:
    temp=1
    print(-1)
elif g%3==0 and s%3!=0:
    temp=1
    print(-1)
elif g%5==0 and s%5!=0:
    temp=1
    print(-1)
elif g%7==0 and s%7!=0:
    temp=1
    print(-1)
else:
    for i in range(1,s):
        a=i*g
        b=s-a
        if b<g:
            break
        if b%g==0:
            print(a,b)
            temp=1
            break


if temp==0:
    print(-1)
