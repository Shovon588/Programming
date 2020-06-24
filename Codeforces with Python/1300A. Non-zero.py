for I in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    res = a.count(0)
    summ = sum(a)+res

    if summ==0:
        res+=1

    print(res)
