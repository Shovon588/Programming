from math import gcd
n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
tempa=1;tempb=1;
for i in a:
    tempa=tempa*i
for i in b:
    tempb=tempb*i

result=gcd(tempa,tempb)
result=str(result)

temp=len(result)
if temp>9:
    print(result[temp-9:])
else:
    print(result)
    
