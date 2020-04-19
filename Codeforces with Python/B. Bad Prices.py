for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a=a[::-1]
    bad=0
    check=a[0]

    for i in a:
        if check<i:
            bad+=1
        check=min(check,i)
    print(bad)
