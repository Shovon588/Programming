n,k=map(int,input().split())
b=list(map(int,input().split()))


a=[];dic={}
#list a contains the unique elements in the array (using this for jumping from one number to another)
#the dictionary contains the frequency of the values, it updates after every iteration
for i in b:
    try:
        if dic[i]:
            dic[i]+=1
    except KeyError:
        dic[i]=1
        a.append(i)
a.sort()

i=0;j=len(a)-1  
while(1):
    frst=a[i];last=a[j]

    if frst==last:
        break
    
    fcost=dic[frst];lcost=dic[last]
    fnxt=a[i+1];lnxt=a[j-1]
    fnxtcost=fnxt-frst;lnxtcost=last-lnxt
    ftotal=fcost*fnxtcost;ltotal=lcost*lnxtcost

    if fcost<=lcost:
        if ftotal<=k:
            i+=1;k-=ftotal;dic[fnxt]+=fcost;dic[frst]=0
        else:
            temp=k//fcost
            frst+=temp;
            k-=(k*temp)
            break
    else:
        if ltotal<=k:
            j-=1;k-=ltotal;dic[lnxt]+=lcost;dic[last]=0
        else:
            temp=k//lcost
            k-=(k*temp)
            last-=temp
            break
        
print(last-frst)
