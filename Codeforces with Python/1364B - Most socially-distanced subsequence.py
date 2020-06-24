for I in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    result = [a[0]]

    for i in range(1,n-1):
        if (a[i]>a[i-1] and a[i]>a[i+1]) or (a[i]<a[i-1] and a[i]<a[i+1]):
            result.append(a[i])

    result.append(a[-1])
    print(len(result))
    print(*result)
