for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    ans=0

    if n==1:
        ans=1
    else:
        for i in range(n-1):
            if a[i+1]-a[i]==1:
                ans=max(ans,2)
            else:
                ans=max(ans,1)
                
    print(ans)
