for _ in range(int(input())):
    n,k,d=map(int,input().split())
    a=list(map(int,input().split()))

    dic={};tot=0
    for i in range(d):
        try:
            if dic[a[i]]:
                dic[a[i]]+=1
        except KeyError:
            dic[a[i]]=1
            tot+=1
    res=tot

    left=0;right=d
    while(right<n):
        dic[a[left]]-=1
        if dic[a[left]]==0:
            tot-=1
        
        try:
            if dic[a[right]]:
                dic[a[right]]+=1
            else:
                dic[a[right]]=1
                tot+=1
        except KeyError:
            dic[a[right]]=1
            tot+=1

        res=min(res,tot)

        left+=1;right+=1
        

    print(res)
