for z in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    one = -1; negone = -1
    try:
        one = a.index(1)
    except ValueError:
        pass

    try:
        negone = a.index(-1)
    except ValueError:
        pass

    flag='YES'
    for i in range(n):
        if a[i]==b[i]:
            pass
        elif a[i]<b[i]:
            if i<=one:
                flag='NO'
        else:
            if i<=negone:
                flag='NO'

    print(flag)
