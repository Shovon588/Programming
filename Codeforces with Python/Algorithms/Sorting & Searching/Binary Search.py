a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

first=0;last=len(a)-1

n = int(input())
result=-1
while first<=last:
    mid=(first+last)//2

    if a[mid]== n:
        result=mid
        break
    elif a[mid]<n:
        first=mid+1
    else:
        last=mid-1

    print (first,last,mid)


if result==-1:
    print('Item not found')
else:
    print('The index is:',result)
