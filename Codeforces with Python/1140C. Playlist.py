n,k=map(int,input().split())
t=[];b=[]
for i in range(n):
    tt,bb=map(int,input().split())
    t.append(tt)
    b.append(bb)

check=[]
for i in range(n):
    temp=b[i]/t[i]
    check.append((temp,i))

check.sort(reverse=True)

time=0;mul=1000000

for i in range(k):
    temp=check[i][1]
    time+=t[temp]
    mul=min(mul,b[temp])

print(time*mul)
