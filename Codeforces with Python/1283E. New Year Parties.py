n=int(input())
a=list(map(int,input().split()))

dic={}

for i in range(n):
    try:
        if dic[a[i]]:
            dic[a[i]]+=1
    except KeyError:
        dic[a[i]]=1

dic2=dic

# Maximize

for x in list(dic):
    if x==a[0]:
        if dic[x]==1:
            try:
                if dic[0]:
                    pass
            except KeyError:
                dic[0]=1
                del dic[x]
        elif dic[x]==2:
            try:
                if dic[0]:
                    pass
            except KeyError:
                dic[0]=1
                dic[1]-=1
        else:
            try:
                if dic[0]:
                    pass
            except KeyError:
                dic[0]=1
                dic[1]-=1

            try:
                if dic[2]:
                    pass
            except KeyError:
                    dic[2]=1
                    dic[1]-=1
        
    elif dic[x]==1:
        pass
    else:
        if dic[x]>2:
            temp = x-1
            try:
                if dic[temp]:
                    pass
            except KeyError:
                dic[temp]=1

            temp = x+1
            try:
                if dic[temp]:
                    pass
            except KeyError:
                dic[temp]=1
        else:
            flag=''
            temp = x-1
            try:
                if dic[temp]:
                    pass
            except KeyError:
                dic[temp]=1
                flag='hoise'

            if flag=='':
                temp = x+1
                try:
                    if dic[temp]:
                        pass
                except KeyErro:
                    dic[temp]=1


Max = len(dic)


# Minimize

res=len(dic)


