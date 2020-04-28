for _ in range(int(input())):
    x,y = map(int,input().split())
    a,b = map(int,input().split())

    x,y = max(x,y),min(x,y)
    
    if 2*a<=b:
        print((x+y)*a)
    else:
        res = 0
        res += (x-y)*a
        res += y*b

        print(res)
