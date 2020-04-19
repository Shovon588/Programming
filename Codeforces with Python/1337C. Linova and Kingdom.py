n, k = map(int,input().split())

check = [0 for i in range(n+1)]

dic = {}
for i in range(n-1):
    u,v = map(int,input().split())
    check[u]=1

    try:
        if dic[u]:
            dic[u].append(v)
            if check[u]!=1:
                try:
                    if dic[v]:
                        dic[v].append(u)
                except KeyError:
                    dic[v]=[u]
    except KeyError:
        dic[u]=[v]
        if check[u]!=1:
            try:
                if dic[v]:
                    dic[v].append(u)
            except KeyError:
                dic[v]=[u]

level = {}








            
