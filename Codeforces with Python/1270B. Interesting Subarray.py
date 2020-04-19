for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))

    temp = []
    Max=(0,0)
    for i in range(n):
        temp.append((a[i],i+1))
        if a[i]>Max[0]:
            Max=(a[i],i+1)            

    res = ''
    for i in range(n):
        if abs(Max[0]-temp[i][0])>abs(Max[1]-temp[i][1]):
            res = (temp[i][1],Max[1])
            break

    if res=='':
        print('NO')
    else:
        print('YES')
        for x in res:
            print(x,end=' ')
        print()
