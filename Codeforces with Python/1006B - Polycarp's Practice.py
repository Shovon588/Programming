n,k = map(int,input().split())

a = list(map(int,input().split()))

b=a[:]

b.sort()

total=0
c=[]
for i in range(n-1,n-k-1,-1):
    total+=b[i]
    c.append(b[i])


day=0
b=[]
for i in range(n):
    if a[i] in c:
        ind=(c.index(a[i]))
        c[ind]=-1
        k-=1
        inda=i+1

        if k==0:
            temp=n-day
        else:
            temp=inda-day
            day=inda

        b.append(temp)

print(total)
for i in range(len(b)):
    print(b[i],end=' ')

        

