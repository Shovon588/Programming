n,k = map(int,input().split())

origin=[];com=[];diff=[]
for i in range(n):
    a,b = map(int,input().split())

    origin.append(a)
    diff.append(a-b)

sum=sum(origin)
diff.sort()
count=0

if sum>k:
    for i in range(n-1,-1,-1):
        sum=sum-diff[i]
        count+=1
        if sum<=k:
            break

if sum<=k:
    print(count)
else:
    print(-1)
