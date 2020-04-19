n=int(input())
b=list(map(int,input().split()))
c=0
a=[]
for i in range(n+1):
    c+=int(b[i])
    a.append(c)

m=int(input())
c=list(map(int,input().split()))

for i in range(m):
    low=0;high=n-1;

    for i in range(n):
        mid=int((low+high)/2)
        print (mid)
