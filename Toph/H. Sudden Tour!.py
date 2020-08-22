def knapsack(cap, n):     
    if n == 0 or cap == 0: 
        return 0
    if memorize[n][cap] != -1: 
        return memorize[n][cap] 

    if weight[n-1] <= cap: 
        memorize[n][cap] = max( 
        cost[n-1] + knapsack(cap-weight[n-1], n-1),knapsack(cap, n-1)) 
        return memorize[n][cap] 
    elif weight[n-1] > cap: 
        memorize[n][cap] = knapsack(cap, n-1) 
        return memorize[n][cap] 
  
for I in range(int(input())):
    n,cap = map(int,input().split())
    weight = []
    cost = []
    for i in range(n):
        w,c = map(int,input().split())
        weight.append(w)
        cost.append(c)

    memorize = [[-1 for i in range(cap + 1)] for j in range(n + 1)]

    result = knapsack(cap, n)

    print("Case %d: %d"%(I+1,result))
