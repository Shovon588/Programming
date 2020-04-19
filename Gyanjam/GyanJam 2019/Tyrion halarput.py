n,m,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

b.sort()
c.sort()


 
def lower(a,b):
    low=0;high=len(a)-1;index=-1

    for i in range(len(a)):
        mid=(high+low)//2

        if low>high:
            index=low
            break

        if a[mid]==b:
            index=mid
            break
        elif a[mid]<b:
            low=mid+1
        else:
            high= mid-1

    return index


result=0

for i in range(n):
    temp=a[i];left=0;right=0;count=0

    res=lower(b,temp)
    print(res)

    left=res
    for j in range(res,-1,-1):
        try:
            if b[j]<temp:
                break
        except IndexError:
            left=j
            break
    print(left)
    res=lower(c,temp)

    right=res
    for j in range(res,k):
        try:
            if c[j]>temp:
                break
        except IndexError:
            right=j
            break


    count=(k-right)+left+1
        
    if count>result:
        result=count
    break


print(result)
    

    

    
