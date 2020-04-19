for i in range(int(input())):
    a,b,n,s=map(int,input().split())

    temp=s//n

    if temp>a:
        temp=a

    temp=s-(temp*n)
    if temp<=b:
        print('YES')
    else:
        print('NO')
