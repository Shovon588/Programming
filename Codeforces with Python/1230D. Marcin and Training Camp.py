n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

dic={};j=0
tempa=[0 for i in range(n)]
tempb=[0 for i in range(n)]
tempc=[0 for i in range(n)]

for i in range(n):
    try:
        tempb[dic[a[i]]]+=b[i]
        tempc[dic[a[i]]]+=1
        
    except KeyError:
        dic[a[i]]=j;j+=1
        tempb[dic[a[i]]]+=b[i]
        tempa[dic[a[i]]]=a[i]
        tempc[dic[a[i]]]+=1


res=0;flag='pass'

for i in range(n):
    if tempc[i]>=2:
        temp=tempb[i]
        if temp>res:
            res=temp
    else:
        temp=0
        flag='dont'

    if flag=='pass':
        for j in range(n):
            if tempa[j]<tempa[i] and i!=j:
                temp+=tempb[j]
                if temp>res:
                    res=temp
    print(res)

print(res)
