a=[5,10,15,20,25,30,35,40,45,50]
b=int(input())

low=0; high=len(a)-1; index=-1;

for i in range(len(a)):
    (mid)=(high+low)/2
    mid=int (mid)
    
    if low>high:
        index=high
        break

    if a[mid]==b:
        index=mid
        break
    elif a[mid]<b:
        low=mid+1
    else:
        high=mid-1
    
print('The lower bound is:',a[index])

