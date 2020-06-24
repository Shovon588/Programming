def makeset(n):
    par[n]=n


def find(r):
    if par[r]==r:return r
    par[r]=find(par[r])
    return find(par[r])


def joint(a,b):
    u = find(a)
    v = find(b)

    if u!=v:
        par[u]=v
        tot = totfriend[u]+totfriend[v]
        totfriend[u] = tot
        totfriend[v] = tot
    print(totfriend[u])

def generate_result(dic):
    res = -1
    for i in range(1,n+1):
        temp = find(i)
        if temp in dic:
            dic[temp]+=1
            res = max(res,dic[temp])
        else:
            dic[temp]=1
            res = max(res,dic[temp])
    return res


nof = 200010
for I in range(int(input())):
    n = int(input())

    par = [None]*(nof+1)
    totfriend = [1]*(nof+1)
    
    for i in range(nof):
        makeset(i+1)

    friends = {}
    count=1
    for i in range(n):
        first, second = map(str,input().split())

        if first not in friends:
            friends[first]=count
            count+=1

        if second not in friends:
            friends[second]=count
            count+=1

        a = friends[first]
        b = friends[second]
        joint(a,b)
        

