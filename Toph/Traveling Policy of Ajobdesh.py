from collections import deque

def dfs(s):
    level=[-1 for i in range(n+1)]
    check=[0 for i in range(n+1)]
    q=deque([])
    q.append(s)
    level[s]=0

    while(len(q))>0:
        u=q.popleft()
        for i in l[u]:
            if level[i]==-1:
                level[i]=level[u]+1
                q.append(i)
    return level


for z in range(int(input())): 
    n,r,c,q=map(int,input().split())

    l=[[] for i in range(n+1)]

    for i in range(r):
        a,b=map(int,input().split())
        l[a].append(b)

    print('Case %d:'%(z+1))
    for i in range(q):
        a,b=map(int,input().split())
        level=dfs(a)

        if level[c]<0 or level[b]<0:
            print('Not possible to go from %d to %d.'%(a,b))
        else:
            result=abs(level[a]-level[c])+abs(level[c]-level[b])
            print('The shortest distance from %d to %d is %d.'%(a,b,result))


        
