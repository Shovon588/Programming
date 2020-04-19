for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))

    day=1;count=0
    res=[0 for i in range(n)]
    dic={}
    for i in range(n):
        dic.update({i+1:a[i]})

    for i in range(n):
        cur=i+1;day=1
        while(1):
            nxt=dic[cur]
            if nxt==i+1:
                res[i]=day
                break
            else:
                day+=1;cur=nxt
    print(*res)
