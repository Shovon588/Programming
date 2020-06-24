for I in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    even = 0
    odd = 0
    for i in range(n):
        if i%2==0 and a[i]%2==1:
            even+=1
        elif i%2==1 and a[i]%2==0:
            odd+=1

    if even!=odd:
        print(-1)
    else:
        if even==0 and odd==0:
            print(0)
        else:
            print(even)
