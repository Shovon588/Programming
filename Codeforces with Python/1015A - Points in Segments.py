n,m = map(int,input().split())

seg=[];check=[];result=[]

for i in range(n):
    l,r = map(int,input().split())

    for j in range(l,r+1):
        seg.append(j)


seg=set(seg)

for i in range(1,m+1):
    check.append(i)

for i in range(m):
    if check[i] not in seg:
        result.append(check[i])
result.sort()

print(len(result))
for i in range(len(result)):
    print(result[i],end=' ')
