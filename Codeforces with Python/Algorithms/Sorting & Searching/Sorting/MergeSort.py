def mergeSort(a,low,high):
    if low<high:
        mid=(low+(high-1))//2
        
        mergeSort(a,low,mid)
        mergeSort(a,mid+1,high)

        merge(a,low,mid,high)
    return a

def merge(a,l,m,r):
    n1=m-l+1
    n2=r-m

    L=[0]*n1
    R=[0]*n2

    for i in range(n1):
        L[i]=a[l+i]
    for i in range(n2):
        R[i]=a[m+1+i]


    i=j=0;k=l

    while i<n1 and j<n2:
        if L[i]<=R[j]:
            a[k]=L[i]
            k+=1;i+=1
        else:
            a[k]=R[j]
            k+=1;j+=1
        

    while i<n1:
        a[k]=L[i];i+=1;k+=1

    while j<n2:
        a[k]=R[j];k+=1;j+=1
    return a

    
a=[5,3,7,43,4,8]
l=0;r=len(a)-1

mergeSort(a,l,r)




#For more: https://www.geeksforgeeks.org/merge-sort/
