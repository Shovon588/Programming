for I in range(int(input())):
    n,k = map(int,input().split())

    if n<=k:
        res = (n*(n-1))//2
        res += 1
    else:
        res = (k*(k+1))//2

    print(res)

    
