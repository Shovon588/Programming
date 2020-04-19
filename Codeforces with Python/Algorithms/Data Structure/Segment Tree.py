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



n=int(input())
a=list(map(int,input().split()))
tree=[0]*(3*n)

func(1,1,n)
