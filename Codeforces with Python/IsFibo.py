from math import sqrt as s
def perfectSqure(x):
    a=s(x)
    a=int(a)
    return a*a==x

def isFibo(n):
    return perfectSqure(5*n*n+4) or perfectSqure(5*n*n-4)

t=int(input())
for _ in range(t):
    m=int(input())
    if isFibo(m)==True:
        print('IsFibo')
    else:
        print('IsNotFibo')
