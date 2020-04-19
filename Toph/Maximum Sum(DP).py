def maxSum(i,tot,count):
    if i==n:
        return tot*count

    ret1=maxSum(i+1,tot+a[i],count+1)
    ret2=maxSum(i+1,tot,count)
    
    return max(ret1,ret2)


for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))

    print(maxSum(0,0,0))
