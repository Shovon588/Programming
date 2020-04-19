n,m,k = map(int,input().split())
a = list(map(int,input().split()))

x=[]
for i in range(n):
    x.append((a[i],i))
x.sort(reverse=True)

total=0;check=[];len=0

for i in range(k*m):
    total+=x[i][0]
    check.append(x[i][1])
    len+=1
        
check.sort()
print(total)
'''
temp=k-1;count=0
for i in range(len):
    count+=1
    if count==m:
        count=0
        print(check[i]+1,end=' ')
        temp-=1

    if temp==0:
        break
'''
count=0
for i in range(1,n,m):
    print(i,end=' ')
    count+=1
    if count==k-1:
        break





