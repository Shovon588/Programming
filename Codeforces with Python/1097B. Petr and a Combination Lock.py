n=int(input())

a=[]
for i in range(n):
    x=int(input())
    a.append(x)
a.sort()

if sum(a)%360==0:
    print('YES')
else:
    flag=0
    for i in range(1,n):
        b=sum(a[:i])
        c=sum(a[i:])

        if b==c:
            print('YES')
            flag=1
            
    if flag==0:print('NO')
