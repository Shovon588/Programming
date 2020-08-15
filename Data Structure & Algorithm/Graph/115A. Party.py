n = int(input())

adj = [[] for i in range(n+1)]

for I in range(n):
    m = int(input())
    if m!=-1:
        adj[I+1].append(m)
        adj[m].append(I+1)

level = [-1 for i in range(n+1)]

def bfs(source):
    que = [source]
    if level[source]==-1:
        level[source]=0

    while len(que)>0:
        cur = que.pop(0)

        for node in adj[cur]:
            if level[node]==-1:
                que.append(node)
                level[node] = level[cur]+1

for I in range(n):
    bfs(I+1)

print(max(level)+1)
