"""
Problem :
Given an array of n elements. We need to answer q queries
telling the sum of elements in range l to r in the array.
Also the array is not static i.e the values are changed
via some point update query.

Range Sum Queries are of form : Q l r , where l is the
starting index r is the ending index

Point update Query is of form : U idx val, where idx is
the index to update val is the updated value
"""

from math import sqrt
    

# 0-indexed query
# Find sum of numbers between l and r
def findSum(l,r):
    leftBlock = l//buck_size
    rightBlock = r//buck_size

    result = 0
    
    if leftBlock==rightBlock:
        for i in range(l,r+1):
            result+=a[i]
    else:
        if l==0 or (l+1)%buck_size==0:
            pass
        else:
            leftBlock+=1
            for i in range(l,(leftBlock*buck_size)):
                result+=a[i]
        
        if (r+1)%buck_size==0:
            rightBlock+=1
        else:
            for i in range(r,(rightBlock*buck_size)-1,-1):
                result+=a[i]

        for i in range(leftBlock,rightBlock):
            result+=bucket[i]
    
    return result


# Update the ind th value of the array with val
def update(ind, val):
    block = ind//buck_size
    bucket[block] = bucket[block]-a[ind]+val
    a[ind]=val


n = int(input())
a = list(map(int,input().split()))

# Make a list of bucket containing sum of each bucket.
buck_size = int(sqrt(n))
bucket = [0 for i in range(buck_size+1)]
segment=0
for i in range(n):
    if i%buck_size==0 and i>0:
        segment+=1
    bucket[segment]+=a[i]

findSum(l,r)
update(ind,val)
