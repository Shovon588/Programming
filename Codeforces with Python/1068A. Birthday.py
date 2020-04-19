n,m,k,l=map(int,input().split())

if m>n:print(-1)
else:
    a=n//m
    b=m*a
    b=b-k
    if b>=l:print(a)
    else:print(-1)
