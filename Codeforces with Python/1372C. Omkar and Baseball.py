for I in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    fromleft=0
    fromright=n-1
    for i in range(n):
        if i+1!=a[i]:
            break
    if i>0:
        fromleft=i

    for i in range(n-1,-1,-1):
        if i+1!=a[i]:
            break

    if i>fromleft:
        fromright=i+1
        
    displaced = 0
    positioned = 0
    for i in range(fromleft,fromright):
        if i+1==a[i]:
            positioned+=1
        else:
            displaced+=1

    if positioned==0 and displaced==0:
        print(0)
    elif positioned==0 and displaced>0:
        print(1)
    elif positioned>0 and displaced>0:
        print(2)
