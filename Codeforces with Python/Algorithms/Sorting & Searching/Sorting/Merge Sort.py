def mergeSort(a,low,high):
    if low<high:
        mid=(low+(high-1))//2

        mergeSort(a,low,mid)
        mergeSort(a,mid+1,high)
        merge(a,low,mid,high)
    return a

def merge(arr,l,m,r):
    n1=m-l+1
    n2=r-m
    L=[0]*n1;R=[0]*n2

    for i in range(n1):
        L[i]=arr[l+i]
    for i in range(n2):
        R[i]=arr[m+1+i]

    i=0;j=0;k=l

    while i<n1 and j<n2:
        if L[i]>=R[j]:
            arr[k]=R[j]
            j+=1;k+=1
        else:
            arr[k]=L[i]
            i+=1;k+=1

    while i<n1:
        arr[k]=L[i]
        k+=1;i+=1
    while j<n2:
        arr[k]=R[j]
        k+=1;j+=1

    return arr

    

a=[5,3,7,43,5,3,7,4,8]
l=0;r=len(a)-1

b=mergeSort(a,l,r)
