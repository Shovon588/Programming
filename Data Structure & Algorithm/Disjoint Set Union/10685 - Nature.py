def makeset(n):
    par[n] = n


def find(r):
    if par[r]==r:
        return r
    par[r] = find(par[r])
    return find(par[r])


def joint(a,b):
    u = find(a)
    v = find(b)

    if u!=v:
        par[u] = v

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

while(1):
    n,m = map(int,input().split())
    if n==0 and m==0:
        break

    par = [None]*(n+1)
    
    animals = {}
    for i in range(n):
        animal = input()
        animals[animal]=i+1
        makeset(i+1)

    for i in range(m):
        first, second = map(str,input().split())
        a = animals[first]
        b = animals[second]
        joint(a,b)

    dic = {}
    result = generate_result(dic)
    print(result)
    s = input()

