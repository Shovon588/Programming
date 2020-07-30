def Lazy(node,low,high,i,j,x):
    if j<low or i>high:
        return
    if low>=i and high<=j:
        tree[node]+=(high-low+1)*x
        lazy[node]+=x
        return
    
    left=2*node
    right=(2*node)+1
    mid=(low+high)//2

    Lazy(left,low,mid,i,j,x)
    Lazy(right,mid+1,high,i,j,x)
    tree[node]=tree[left]+tree[right]+((high-low+1)*lazy[node])


def query(node,b,e,i,j,carry=0):
    if i>e or j<b:
        return 0

    if b>=i and e<=j:
        return tree[node] + carry*(e-b+1)

    left = 2*node
    right = (2*node)+1
    mid = (b+e)//2

    p1 = query(left,b,mid,i,j,carry+lazy[node])
    p2 = query(right,mid+1,e,i,j,carry+lazy[node])

    return p1+p2


n,m = map(int,input().split())

tree=[0 for i in range(3*n)]
lazy=[0 for i in range(3*n)]


for i in range(m):
    left,right,val = map(int,input().split())
    Lazy(1,1,n,left,right,val)

res = -1
for i in range(1,n+1):
    temp = query(1,1,n,i,i)
    res = max(res,temp)
    






    








