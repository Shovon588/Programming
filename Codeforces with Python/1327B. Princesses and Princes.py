for _ in range(int(input())):
    n = int(input())
    princess = []
    prince = [-1]

    for i in range(n):
        princess.append(list(map(int,input().split())))
        prince.append(-1)

    improve = 0
    for i in range(n):
        flag='yo'
        for j in range(1,princess[i][0]+1):
            if prince[princess[i][j]]==-1:
                prince[princess[i][j]]=1
                flag='okay'
                break

        if flag=='yo':
            improve = i+1

    flag=''
    if improve!=0:
        for i in range(1,len(prince)):
            if prince[i]==-1:
                print('IMPROVE')
                print(improve,i)
                flag='done'
                break
        if flag=='':
            print('OPTIMAL')
    else:
        print('OPTIMAL')
        
