def segTree(node,low,high):
    if low==high:
        tree[node]=a[low-1]
        return
    left=2*node
    right=(2*node)+1
    mid=(low+high)//2

    segTree(left,low,mid)
    segTree(right,mid+1,high)
    tree[node]=min(tree[left],tree[right])

def query(node,low,high,i,j):
    if low>=i and high<=j:
        return tree[node]
    if j<low or i>high:
        return 0
    
    left=2*node
    right=(2*node)+1
    mid=(low+high)//2
    q1=query(left,low,mid,i,j)
    q2=query(right,mid+1,high,i,j)
    if q1>0 and q2>0:
        return min(q1,q2)
    else:
        return q1+q2
    

for i in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    tree=[0]*(3*n)
    segTree(1,1,n)
    print('Case %d:'%(i+1))
    for j in range(m):
        a,b=map(int,input().split())
        print(query(1,1,n,a,b))
        
