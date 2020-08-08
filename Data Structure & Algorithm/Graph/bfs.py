def find_path(dest):
    path = [dest]

    while(1):
        par = parent[dest]
        path.append(par)
        dest = par

        if dest==source:
            break
    return path[::-1]


def find_depth(node):
    return parent[node]


print('Enter number of vertex and edges:')
v,e = map(int,input().split())

adj = [[] for i in range(v+1)] 
level = [-1 for i in range(v+1)]
parent = [-1 for i in range(v+1)]


print('Enter the connections between the vertex:')
for i in range(e):
    start, end = map(int,input().split())
    adj[start].append(end)
    adj[end].append(start)



source = 6
que = [source]
level[source] = 0
parent[source] = source

while len(que)>0:
    cur = que.pop(0)
    
    for node in adj[cur]:
        if level[node]==-1:
            que.append(node)
            level[node]=level[cur]+1
            parent[node] = cur
    
