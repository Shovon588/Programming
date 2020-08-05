for I in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    mincan = min(a)
    minor = min(b)

    result = 0
    for i in range(n):
        candiff = abs(mincan-a[i])
        ordiff = abs(minor-b[i])

        temp = min(candiff,ordiff)
        temp += max(candiff,ordiff) - temp

        result+=temp

    print(result)
