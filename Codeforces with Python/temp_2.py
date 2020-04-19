def king(i,w,amount):
    if i==n or w==K:
        if amount==bud and w==K:return 1
        else:return 0

    if dp[i][amount]!=0:
        return dp[i][amount]
    
    ret1=0;ret2=0
    if w+weight[i]<=K:
        ret1=king(i+1,w+1,amount+cost[i])
    ret2=king(i+1,w,amount)

    dp[i][amount]=ret1+ret2

    return dp[i][amount]


for i in range(int(input())):
    n=int(input())
    K=int(input())
    bud=int(input())
    cost=list(map(int,input().split()))
    weight=[1 for i in range(n+1)]

    dp=[[0 for i in range(sum(cost)+1)]for j in range(n+1)]

    ans=king(0,0,0)

    print("Case %d: %d"%(i+1,ans))
