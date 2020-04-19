from math import sqrt as s
n=int(input())
temp=int(s(n))
div=n
for i in range(2,temp+1):
    if n%i==0:
        div=i
        break

if div==n:
    print(div)
else:
    print(n//div)
