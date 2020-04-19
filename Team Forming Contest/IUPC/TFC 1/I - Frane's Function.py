from math import sqrt

n=int(input())
s=int(sqrt(n))

temp=1
for i in range(2,s+1):
    if n%i==0:
        temp=n//i
        break

if temp>=n-1:
    print(n-1)
else:
    print(n-temp)
