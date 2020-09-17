for I in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    ones = 0
    zeros = 0
    for num in a:
        if num==1:ones+=1
        else:zeros+=1

    half = n//2

    if zeros>=half:
        print(half)
        for i in range(half):
            print(0,end=' ')
    elif ones>=half:
        if half%2==1:
            print(half+1)
            for i in range(half+1):
                print(1,end=' ')
        else:
            print(half)
            for i in range(half+1):
                print(1,end=' ')
    print()
