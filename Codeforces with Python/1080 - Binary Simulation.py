a='10011'
n=5
tree=[2]*(3*n)

def segTree(node,low,high):
    if low==high:
        if a[low-1]=='0':
            tree[node]=0
        else:
            tree[node]=1
        return
    left=2*node
    right=(2*node)+1
    mid=(low+high)//2
    
    segTree(left,low,mid)
    segTree(right,mid+1,high)

segTree(1,1,n)
    
