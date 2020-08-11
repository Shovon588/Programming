def bfs(source, destination):
    x = [-2,-2,2,2,-1,1,-1,1]
    y = [1,-1,1,-1,2,2,-2,-2]

    level = {}
    que = [source]
    level[source]=0

    while len(que)>0:
        cur = que.pop(0)

        for i in range(8):
            tempi,tempj = cur[0]+x[i], cur[1]+y[i]
            if is_valid(tempi,tempj):
                if (tempi,tempj) not in level:
                    que.append((tempi,tempj))
                    level[(tempi,tempj)] = level[cur]+1
                    #print(cur, '-> ',(tempi,tempj))

            if destination in level:
                return level[destination]

            

def is_valid(x,y):
    if x>=1 and x<=8 and y>=1 and y<=8:
        return True
    return False



for_j = 'abcdefgh'
for I in range(int(input())):
    src, dest = map(str,input().split())
    srci,srcj = int(src[1]), for_j.index(src[0])+1
    desti,destj = int(dest[1]), for_j.index(dest[0])+1
    
    source = (srci,srcj)
    destination = (desti,destj)

    print(bfs(source,destination))









                
