for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))

    odd=0
    for i in a:
        if i%2==1:odd+=1

    if odd%2==1 or (odd!=0 and odd!=n):
        print('YES')
    else:
        print('NO')
