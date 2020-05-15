for _ in range(int(input())):
    n,k = map(int,input().split())

    odd = n-(k-1)
    even = n-((k-1)*2)

    if odd>0 and odd%2==1:
        print('YES')
        for i in range(k-1):
            print(1,end=' ')
        print(n-(k-1))
    elif even>0 and even%2==0:
        print('YES')
        for i in range(k-1):
            print(2,end=' ')
        print(n-((k-1)*2))
    else:
        print('NO')
