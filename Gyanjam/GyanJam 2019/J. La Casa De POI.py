from math import sqrt as s
a,b=map(int,input().split())

min=min(a,b)
max=max(a,b)

temp=int(s(min))

sum=0
for i in range(1,temp+1):
    if min%i==0 and max%i==0:
        sum+=i
        t=min//i
        if max%t==0 and t!=temp:
            sum+=t
    elif min%i==0 and max%i!=0:
        t=min//i
        if max%t==0:
            sum+=t

if min==1:
    print(1)
else:
    print(sum)
        
