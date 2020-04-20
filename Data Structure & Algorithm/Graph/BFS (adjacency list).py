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

que = [] # Queue to push nodes or pop from

starting = 1 # starting node
ending = 2

que.append(starting) # appending the starting the node to the queue
visited[starting]=1 # marking the starting node as visited
route = [] # declaring the list to keep track of the route

count=1
while(len(que)>0):
    cur = que.pop() # popping the last element from queue
    for i in range(len(adj[cur])): # Traversing each of its neighbours
        neighbour = adj[cur][i]
        if visited[neighbour]==0: # Checking if the current neighbour is visited or not
            visited[neighbour]=1 # If not then marking it as visited
            que.append(neighbour) # And appending it to the queue for further checking
        print(count)
        count+=1

    route.append(cur) # Adding the current path to the route
    if cur==ending:
        break

print("Traversing route:")
print(*route)



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
