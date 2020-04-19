def dp(i,arr):
    if i==n:
        return len(arr)

    if a[i]>arr[-1]:
        arr.append(a[i])
        temp1=dp(i+1,arr)
        arr.pop()
    else:
        temp1=len(arr)

    temp2=dp(i+1,arr)

    return max(temp1,temp2)
    
n=int(input())
a=list(map(int,input().split()))
arr=[0]


res = dp(0,arr)
print(res-1)
