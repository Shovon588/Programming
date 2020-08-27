print('Enter number of vertex and edges:')
v,e = map(int,input().split())

adj = [[] for i in range(v+1)] # Creating an empty list for adjacency list
level = [0 for i in range(v+1)] # Creating a list for visited nodes


print('Enter the connections between the vertex:')
for i in range(e):
    start, end = map(int,input().split())
    adj[start].append(end)
    adj[end].append(start)
    
    # Creating the adjacency list (bidirectional)

que = [] # Queue to push nodes or pop from

starting = 6 # starting node
ending = 3


que.append(starting) # appending the starting the node to the queue
level[starting]=1 # marking the starting node as visited
parent = [-1 for i in range(v+1)] # declaring the list to keep track of the route

while(len(que)>0):
    cur = que.pop(0) # popping the first element from queue
    for i in range(len(adj[cur])): # Traversing each of its neighbours
        neighbour = adj[cur][i]
        if level[neighbour]==0: # Checking if the current neighbour is visited or not
            level[neighbour]=level[cur]+1 # If not then marking it as visited
            que.append(neighbour) # And appending it to the queue for further checking
            parent[neighbour]=cur
            

route = []
route.append(ending)
for i in range(len(parent)):
	temp = parent[ending]
	print(temp)
	route.append(temp)
	ending=temp
	
	if temp==starting:
		break

route = route[::-1]

print("Traversing route:")
print(*route)

"""
Test case:
10 13
1 2
1 3
1 4
2 6
6 10
4 7
3 7
3 8
7 9
7 8
8 5
5 10
9 10

From: http://www.shafaetsplanet.com/?p=604
"""
