from math import ceil
n,p1,p2,k = map(int,input().split())
a = list(map(int,input().split()))

combo=p1+p2
cost=[]
for mons in a:
    if mons%combo==0:
        temp = p2
        res = ceil(temp/p1)
    else:
        temp = mons%combo
        if temp>p1:
            temp=temp-p1
            res=ceil(temp/p1)
        else:
            res=0
    
    cost.append(res)

cost.sort()

count=0;res=0
for i in range(n):
    if count+cost[i]<=k:
        count+=cost[i]
        res+=1
    
print(res)
