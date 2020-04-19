a=[4,5,6,7,8]
n=len(a)
tree=[0]*(3*n)
lazy=[0]*(3*n)

def segTree(node,low,high):
    if low==high:
        tree[node]=a[low-1]
        return
    left=2*node
    right=(2*node)+1
    mid=(low+high)//2
    segTree(left,low,mid)
    segTree(right,mid+1,high)
    tree[node]=tree[left]+tree[right]

segTree(1,1,n)

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

print(tree)

Lazy(1,1,n,2,4,100)
