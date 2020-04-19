l=[];i=1;count=0
while(1):
    count+=i
    l.append(count)
    i+=1
    if count>1000000005:
        break

def find(n):
    low=0;high=44720;index=-1

    while(1):
        mid=(low+high)//2

        if low>high:
            index=high
            break

        if l[mid]==n:
            index=mid
            break
        elif l[mid]<n:
            low=mid+1
        else:
            high=mid-1
    return index
    



for _ in range(int(input())):
    n,m=map(int,input().split())
    dif=abs(n-m)

    if dif==0:
        print(0)
    else:
        temp=find(dif)
        while(1):
            temp2=(temp*(temp+1))//2
            if temp2<dif:
                temp+=1
            elif (temp2+n+m)%2==0:
                    print(temp)
                    break
            else:
                temp+=1
