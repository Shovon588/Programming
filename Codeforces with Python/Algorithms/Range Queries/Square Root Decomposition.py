from math import sqrt as s

a=[1,2,3,4,5,6,7,8,9]
size=int(s(len(a)))

segment=[0 for i in range(size+1)]
seg=int(len(a)//size)

curSeg=-1
for i in range(len(a)):
    if i%size==0:
        curSeg+=1
    segment[curSeg]+=a[i]


def query(l,r):
    l-=1;r-=1 #zero indexed
    total=0
    while l<r and l%size!=0:
        total+=a[l]
        l+=1

    while(l+size<=r):
        total+=segment[l//size]
        l+=size

    while l<=r:
        total+=a[l]
        l+=1
    return total

def update(i,val):
    i-=1 #zero indexed
    temp=i//size
    segment[temp]-=a[i]
    segment[temp]+=val
    a[i]=val
    
