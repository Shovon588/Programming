import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

n=int(input())
a=list(map(int,input().split()))
a.sort()
b,c=a[0],a[n-1]

print(c-b,end=" ")

if b!=c:
    b,c=a.count(b),a.count(c)
    print(b*c)
else:
     b=a.count(b)
     print(int(ncr(b,2)))
