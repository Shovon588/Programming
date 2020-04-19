print('Enter number of vertex and edges:')
v,e = map(int,input().split())

adj = [[] for i in range(v+1)] # Creating an empty list for adjacency list
visited = [0 for i in range(v+1)] # Creating a list for visited nodes

print('Enter the connections between the vertex:')
for i in range(e):
    start, end = map(int,input().split())
    adj[start].append(end)
    adj[end].append(start)
    
    # Creating the adjacency list (bidirectional)

starting = 1
route = []

def DFS(node):
    if visited[node]==1:return

    visited[node]=1
    route.append(node)
    
    for i in range(len(adj[node])):
        DFS(adj[node][i])

DFS(starting)


"""
Test case:
7 7
6 4
4 5
4 3
3 2
2 5
5 1
2 1

Resulting traverse:
[6, 4, 3, 2, 1, 5]
"""
