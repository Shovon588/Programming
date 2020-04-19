for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    
    res=0
    for i in range(0,2*n,2):
        temp = abs(a[i]-a[i+1])
        res = max(res,temp)

    print(res)
