# Number of nodes
n = 5

# Make a empty list same size as the node size.
par = [None]*(n+1)

def makeset(n):
    """
    Returns a list where each node is its own parent.
    """
    par[n] = n

def find(r):
    """
    Returns a nodes representitive.
    """
    # If the node is its own parent.
    if par[r]==r: return r

    # Check the parent of the parent is the node is not its own parent.
    par[r] = find(par[r])
    return find(par[r])


# Makes the list where each node is own parent.
for i in range(1,n+1):
    makeset(i)


# Checks the connection between two nodes and assigns a parent in it.
for i in range(int(input())):
    a,b = map(int,input().split())
    u = find(a)
    v = find(b)

    if u==v:
        print("Already friend")
    else:
        par[u] = v
