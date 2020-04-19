n,m=map(int,input().split())

a = list(map(int,input().split()))

b=[]
c=[]
for i in range(n):
    if a[i] not in c:
        b.append(a.index(a[i])+1)
        c.append(a[i])


if len(c)>=m:
    print ('YES')
    for i in range(m):
        print(b[i],end=' ')
else:
    print('NO')
