for I in range(int(input())):
    x,y,n = map(int,input().split())

    temp = n//x

    if (temp*x)+y<=n:
        print(temp*x+y)
    else:
        print((temp-1)*x+y)
