for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort(reverse=True)

    res=0
    for i in range(n):
        temp=min(i+1,a[i])
        res=max(res,temp)

    print(res)
