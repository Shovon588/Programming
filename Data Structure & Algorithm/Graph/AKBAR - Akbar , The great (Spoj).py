def bfs(source, strength):
    dic = {}
    
    que = [source]
    guard[source] += 1
    dic[source]=0

    while len(que)>0:
        cur = que.pop(0)
        
        for node in adj[cur]:
            if node not in dic:
                if dic[cur]+1>strength:
                    break
                que.append(node)
                guard[node]+=1
                dic[node]=dic[cur]+1


for _ in range(int(input())):
    city,road,soldier = map(int,input().split())

    adj = [[] for i in range(city+1)]
    guard = [0 for i in range(city+1)]

    for I in range(road):
        u,v = map(int,input().split())
        adj[u].append(v)
        adj[v].append(u)


    for I in range(soldier):
        source, strength = map(int,input().split())
        bfs(source,strength)


    flag='Yes'

    for num in guard[1:]:
        if num==0 or num>1:
            flag='No'
            break

    print(flag)
