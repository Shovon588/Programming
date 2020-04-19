n=int(input())
b=list(map(int,input().split()))

dic={};a=[]
for i in b:
    try:
        if dic[i]:
            dic[i]+=1
    except KeyError:
        dic[i]=1
        a.append(i)
a.sort()
n=len(a)
res=0

for i in range(n):
    left=max(0,i-3)
    right=min(i+2,n-1)+1
    count=0
    for j in range(left,right):
        if abs(a[left]-a[j])<=5:
            count+=dic[a[j]]
        else:
            break
    res=max(res,count)
print(res)
