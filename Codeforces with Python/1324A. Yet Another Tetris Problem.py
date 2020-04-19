for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))

    flag='okay'
    if n>=1:
        for i in range(n-1):
            temp = abs(a[i]-a[i+1])
            if temp%2==1:
                flag='not okay'
                break

    if flag=='okay':
        print('YES')
    else:
        print('NO')
