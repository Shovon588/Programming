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
    return tree

def query(node,low,high,i,j):
    if low>=i and high<=j:
        return tree[node]
    if i>high or j<low:
        return 0
    left=2*node
    right=(2*node)+1
    mid=(high+low)//2

    p1=query(left,low,mid,i,j)
    p2=query(right,mid+1,high,i,j)
    return p1+p2



def update(node,low,high,i,new):
    if i<low or i>high:
        return 0
    if low>=i and high<=i:
        tree[node]=new
        return

    left=2*node
    right=(2*node)+1
    mid=(low+high)//2

    update(left,low,mid,i,new)
    update(right,mid+1,high,i,new)
    tree[node]=tree[left]+tree[right]
    return tree


n=int(input())
a=list(map(int,input().split()))
tree=[0]*(3*n)

print(segTree(1,1,n))
print('The sum of 2 to 5 is:',query(1,1,n,2,5))
print(update(1,1,n,1,100))
