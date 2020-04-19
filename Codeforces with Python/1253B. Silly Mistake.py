n=int(input())
a=list(map(int,input().split()))

dic={};flag='ok';count=0;tot=0;res=[]

for i in a:
    if i>0:
        try:
            if dic[i]>=0:
                flag='dismiss'
                break
        except KeyError:
            dic[i]=1
            count+=1

    else:
        try:
            if dic[abs(i)]==1:
                dic[abs(i)]=0
                count-=1
            elif dic[abs(i)]==0:
                flag='dismiss'
                break
        except KeyError:
            flag='dismiss'
            break
    tot+=1
    if count==0:
        res.append(tot)
        tot=0;count=0;dic={}


if flag=='dismiss' or len(res)==0 or count>0:
    print(-1)
else:
    print(len(res))
    print(*res)
