n=int(input())
s=input()

res=[[] for i in range(n)]


for i in range(n):
    a,b=map(int,input().split())
    zero=[0]*a
    one=[1]*a
    first=[int(s[i])]*b
    
    temp=int(s[i])

    res[i].extend(first)

    for j in range(1000):
        if temp==1:
            temp=0
            res[i].extend(zero)
        else:
            res[i].extend(one)
            temp=1

minb=1000
for i in range(n):
    minb=min(minb,len(res[i]))
    


result=0
for i in range(minb):
    count=0
    for j in range(n):
        count+=res[j][i]
        result=max(result,count)

print(result)
