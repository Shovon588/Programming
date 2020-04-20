def knap(i,w):
    if i==n:
        return 0
    print(i)
    
    if w+weight[i]<=cap:
        profit1=cost[i]+knap(i+1,w+weight[i])
    else:
        profit1=0

    profit2=knap(i+1,w)

    return max(profit1,profit2)


n,cap=map(int,input().split())
weight=list(map(int,input().split()))
cost=list(map(int,input().split()))



'''
Input:
4 10
1 4 3 4
120 280 150 200

Output should be 600

'''
