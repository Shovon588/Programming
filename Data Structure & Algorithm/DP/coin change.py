coin=[5,3,2]


def call(i,amount):
    if i>=len(coin):
        if amount==make:return 1
        else:return 0

    if dp[i][amount]!=0:return dp[i][amount]

    ret1=0;ret2=0
    if amount+coin[i]<=make:
        ret1=call(i,amount+coin[i])
    ret2=call(i+1,amount)

    print(i,amount,ret1,ret2)
    dp[i][amount]=ret1+ret2
    return dp[i][amount]
        

for i in range(int(input())):
    make=int(input())
    dp=[[0 for i in range(make+1)]for j in range(len(coin)+1)]

    print(call(0,0))
    
