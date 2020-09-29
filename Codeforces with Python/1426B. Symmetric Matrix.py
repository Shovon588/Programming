for I in range(int(input())):
    n,m = map(int,input().split())

    type1 = False
    for i in range(n):
        a1,a2 = map(int,input().split())
        a3,a4 = map(int,input().split())

        if a2 == a3:
            type1 = True


    if type1 and m%2!=1:
        print('YES')
    else:
        print("NO")
        
