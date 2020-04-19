from numpy import cumsum as cum

n,a,b=map(int,input().split())
x=list(map(int,input().split()))

for i in range(1,n):
    x[i]=x[i]+x[i-1]

print(x[b]-x[a-1])
