n=int(input())
from math import sqrt as s
def isPerfect(n):
    a=s(n)
    a=int(a)
    return a*a==n

a=isPerfect(n)
print(a)
