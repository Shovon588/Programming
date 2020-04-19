n,k,m = map(int,input().split())

a=list(map(int,input().split()))

a.sort()
sum=0
if m>=n and k<=m:
    print(a[-1]+k)
elif m>=n and k>m:
    print(a[-1]+(m-(n-1)))
else:
    for i in range(m,n):
        sum+=a[i]
    print(sum/(n-m))
