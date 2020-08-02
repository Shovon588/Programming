def power(a,b,m):
    result = 1
    a = a%m
    while b>0:
        if b%2==1:
            result = (result*a)%m
        a = (a*a) % m
        b = b//2

    return result%m



for I in range(int(input())):
    a,b = map(int,input().split())

    print(power(a,b,10))
