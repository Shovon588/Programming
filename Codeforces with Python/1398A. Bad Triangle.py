for I in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    temp = a[0]+a[1]

    res = -1
    for i in range(2,n):
        if a[i]>=temp:
            res = i+1
            break

    if res==-1:
        print(res)
    else:
        print(1,2,res)
