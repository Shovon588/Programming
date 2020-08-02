def power(a,b,m):
    result = 1
    print(a,m,'a')
    a = a%m
    while b>0:
        if b%2==1:
            result = (result*a)%m
        a = (a*a) % m
        b = b//2

    return result%m


while True:
    try:
        a = input()
        if a=='':
            pass
        else:
            b = int(input())
            m = int(input())
            a = int(a)
            print(power(a,b,m))

    except EOFError:
        break

