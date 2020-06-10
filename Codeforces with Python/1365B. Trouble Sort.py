for I in range(int(input())):
    n = input()
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    zeros = 0
    ones = 0
    for num in b:
        if num==1:
            ones+=1
        else:
            zeros+=1

    if ones>0 and zeros>0:
        print('YES')
    else:
        c=a[::]
        a.sort()
        if a==c:
            print('YES')
        else:
            print('NO')
