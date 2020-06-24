for I in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))

    left = 10000005
    right = -1

    count = 0

    for i,num in enumerate(a):
        if num%k==0:
            count+=1
        else:
            left = min(left,i)
            right = max(right,i)


    if sum(a)%k!=0:
        print(n)
    elif count==n:
        print(-1)
    else:
        fromLeft = abs(0-left)+1
        fromRight = n-right

        if fromLeft<=fromRight:
            print(n-fromLeft)
        else:
            print(n-fromRight)
