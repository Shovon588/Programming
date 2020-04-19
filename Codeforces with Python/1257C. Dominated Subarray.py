for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    dic={}

    for i in range(n):
        try:
            if dic[a[i]]:
                dic[a[i]].append(i)
        except KeyError:
            dic[a[i]]=[i]

    res=200005
    for i in dic:
        temp=dic[i]
        for j in range(len(temp)-1):
            res=min(res,temp[j+1]-temp[j])

    if res>n:
        print(-1)
    else:
        print(res+1)
