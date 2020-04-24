t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    res = []

    for i in range(n):
        if i==0:
            res.append(a[0])
        else:
            if a[i]<0 and res[-1]<0:
                res[-1]=max(res[-1],a[i])
            elif a[i]>0 and res[-1]>0:
                res[-1]=max(res[-1],a[i])
            else:
                res.append(a[i])
        
    
    print(sum(res))
            
        
