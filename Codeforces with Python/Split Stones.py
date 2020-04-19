for i in range(int(input())):
    a,b,c,x,y = map(int,input().split())

    sum1=a+b+c
    sum2=x+y

    if sum1!=sum2:
        print('NO')
    elif min(a,b,c)>min(x,y):
        print('NO')
    else:
        print('YES')
