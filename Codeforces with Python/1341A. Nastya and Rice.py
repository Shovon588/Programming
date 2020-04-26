for _ in range(int(input())):
    n,a,b,c,d = map(int,input().split())
    left = a-b
    right = a+b
    mini = c-d
    maxi = c+d

    if n*right<mini or n*left>maxi:
        print('NO')
    else:
        print('YES')
