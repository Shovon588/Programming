from sys import stdout,stdin
 
input=stdin.buffer.readline

def segment_tree(node, low, high):
    if low==high:
        tree[node]=a[low-1]
        return

    mid = (low+high)//2
    left = 2*node
    right = (2*node)+1
    
    segment_tree(left,low,mid)
    segment_tree(right, mid+1,high)
    tree[node] = tree[left]+tree[right]

    
def update(node,low,high,index,value):
    if index<low or index>high:
        return 0
    if low==index and high==index:
        tree[node]=value
        return

    left = 2*node
    right = (2*node)+1
    mid = (low+high)//2
    update(left,low,mid,index,value)
    update(right,mid+1,high,index,value)
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


n,m = map(int,input().split())
a = list(map(int,input().split()))

tree = [0] * (4*n)
segment_tree(1,1,n)

for i in range(m):
    a,b,c = map(int,input().split())
    if a==1:
        update(1,1,n,b+1,c)
    else:
        res = query(1,1,n,b+1,c)
        stdout.write(str(res)+'\n')
        
    
