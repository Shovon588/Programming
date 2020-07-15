def func(node,low,high):
    if low==high:
        tree[node]=a[low-1]
        return
    
    left=2*node
    right=(2*node)+1
    mid=(low+high)//2
    func(left,low,mid)
    func(right,mid+1,high)
    tree[node]=tree[left]+tree[right]


def query(node,b,e,i,j):
    if b>=i and e<=j:
        return tree[node]

    if i>e or j<b:
        return 0

    left=2*node
    right=(2*node)+1
    mid=(b+e)//2

    p1=query(left,b,mid,i,j)
    p2=query(right,mid+1,e,i,j)
    return p1+p2



n=int(input())
a=list(map(int,input().split()))
tree=[0]*(3*n)
func(1,1,n)

for i in range(int(input())):
    l,m=map(int,input().split())

    b=query(1,1,n,l,m)
    print(b)
