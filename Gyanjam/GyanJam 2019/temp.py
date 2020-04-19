n,m,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

a=list(set(a))
b=list(set(b))
c=list(set(c))

b.sort()
c.sort()

n,m,k=len(a),len(b),len(c)

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
    temp=a[i];count=0

    res1=lower(b,temp)
    count+=res1

    res2=lower(c,temp)
    
    if res2>=k:
        pass
    elif c[res2]==temp:
        count+=k-(res2+1)
    else:
        count+=k-res2

    count+=1

    if count>result:
        result=count
            
print(result)

    
    
