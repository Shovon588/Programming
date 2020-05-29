for I in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()

    result = 0
    for i in range(n-1,-1,-1):
        if i+1>=a[i]:
            result+=i+1
            break

    print(result+1)
