n,k=map(int,input().split())
a=list(map(int,input().split()))

a.sort(reverse=True)

if k>n:
    print(a[-1])
else:
    print(a[k-1])
