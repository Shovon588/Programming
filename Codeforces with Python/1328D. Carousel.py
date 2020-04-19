from math import ceil
for _ in range(int(input())):
    dic = {}
    
    n = int(input())
    a = list(map(int,input().split()))
    a.append(a[0])

    res = [1]
    col = 1
    cur = 1
    for i in range(1,n-1):
        if a[i]==a[i-1]:
            res.append(cur)
        else:
            col=2
            if cur==1:
                res.append(2)
                cur=2
            else:
                res.append(1)
                cur=1

    if a[n-1]!=a[n] and a[n-1]!=a[n-2] and a[n-2]!=a[n]:
        res.append(3)
        col=3
    elif a[n-1]!=a[n] and a[n-1]!=a[n-2]:
        if res[-1]==1:
            res.append(2)
        else:
            res.append(1)
    elif a[n-2]==a[n-1]:
        res.append(res[-1])
    elif a[n-1]==a[n]:
        res.append(res[0])
    

    print(col)
    print(*res)
