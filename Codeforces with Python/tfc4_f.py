n,k=map(int,input().split())

match=0;a=[]
for i in range(n):
    match+=i
for i in range(1,n+1):
    a.append(i)

if k*2>=n:
    print(-1)
else:
    print(n*k)
    temp=match//n
    a=a*(temp+1)
    for i in range(n):
        for j in range(1,k+1):
            print(a[i],a[i+j])
