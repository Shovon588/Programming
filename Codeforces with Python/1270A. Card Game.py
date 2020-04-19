for i in range(int(input())):
    n,k1,k2=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    first = max(a)
    second = max(b)

    if first>second:
        print("YES")
    else:
        print('NO')
