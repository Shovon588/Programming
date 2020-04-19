from math import sqrt as s
n=int(input())

i=2;result=1
while i<=s(n):
    if n%i==0:
        if n//i==i:result+=i
        else:result+=i+(n//i)
        print(i,n//i)
    i+=1

print(result)
