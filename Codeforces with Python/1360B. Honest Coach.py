for ii in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()

    res = 1000000005
    for i in range(n-1):
        res = min(res,abs(a[i]-a[i+1]))
    print(res)
