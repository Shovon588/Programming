#problem: https://www.spoj.com/problems/MULTQ3/

from sys import stdin,stdout

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

def Lazy(node,low,high,i,j,x):
    if j<low or i>high:
        return
    if low>=i and high<=low:
        tree[node]+=(high-low+1)*x
        lazy[node]+=x
        return
    left=2*node
    right=(2*node)+1
    mid=(low+high)//2

    Lazy(left,low,mid,i,j,x)
    Lazy(right,mid+1,high,i,j,x)
    tree[node]=tree[left]+tree[right]+((high-low+1)*lazy[node]) 


def query(node,low,high,i,j):
    if low>j or high<i:
        return 0
    if low==high:
        if tree[node]%3==0:
            return 1
        return 0
    
    left=2*node
    right=(2*node)+1
    mid=(low+high)//2
    
    q1=query(left,low,mid,i,j)
    q2=query(right,mid+1,high,i,j)
    return q1+q2

n,m=map(int,stdin.readline().split())
a=[0]*n
tree=[0]*(3*n)
lazy=[0]*(3*n)

segTree(1,1,n)

for _ in range(m):
    x,y,z=map(int,stdin.readline().split())
    if x==0:
        Lazy(1,0,n-1,y,z,1)
    else:
        b=query(1,0,n-1,y,z)
        stdout.write('%d\n'%(b))
        
