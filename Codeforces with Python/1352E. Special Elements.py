t=int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    dic={}
    for i in l:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    ans=0
    for i in range(n):
        s=l[i]
        for j in range(i+1,n):
            s+=l[j]
            if s in dic:
                ans += dic[s]
                dic[s]=0
    print(ans)
