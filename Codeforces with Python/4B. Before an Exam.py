n,T=map(int,input().split())
from math import ceil

minT=[];maxT=[]
for i in range(n):
    a,b=map(int,input().split())
    minT.append(a)
    maxT.append(b)
    
suma=sum(minT);sumb=sum(maxT)
result=[]

temp=T/n;khuchra=0

if sumb<T or suma>T:
    print('NO')
elif suma==T:
    print('YES')
    for i in range(n):
        print(minT[i],end=' ')
elif sumb==T:
    print('YES')
    for i in range(n):
        print(maxT[i],end=' ')
else:
    print('YES')
    for i in range(n):
        if temp>=minT[i] and temp<=maxT[i]:
            print(ceil(temp),end=' ')
        if temp>maxT[i]:
            print(maxT[i],end=' ')
            khuchra+=maxT[i]-ceil(temp)
