for I in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    
    flag='YES'
    for i in range(n-1):
        if abs(a[i]-a[i+1])>1:
            flag='NO'
            break

    print(flag)
