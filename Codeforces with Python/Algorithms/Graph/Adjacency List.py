from collections import deque
n,e=map(int,input().split())


dic={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'J',9:'K'}

l=[[] for i in range(n+1)]

for i in range(e):
    a,b=map(int,input().split())
    l[a].append(b)


level=[-1 for i in range(n+1)]
check=[0 for i in range(n+1)]

q=deque([])
path=[[] for i in range(n+1)]

def dfs(n):
    q.append(n)
    level[n]=0

    while(len(q))>0:
        u=q.popleft()
        for i in l[u]:
            if level[i]==-1:
                level[i]=level[u]+1
                q.append(i)
                print(i)
 
    return level
        
