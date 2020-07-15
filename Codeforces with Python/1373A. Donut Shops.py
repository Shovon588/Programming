for I in range(int(input())):
    a,b,c = map(int,input().split())

    onepiece = c/b
    onebox = a*b

    if a<c:
        first = 1
    else:
        first = -1

    if c<a*b:
        second = b
    else:
        second = -1

    
    print(first,second)
