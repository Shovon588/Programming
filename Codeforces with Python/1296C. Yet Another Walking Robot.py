for _ in range(int(input())):
    n=int(input())
    s = input()

    dic={}
    x,y=0,0
    dic[0,0] = [0]

    least=10000000;res=[]
    for i in range(n):
        if s[i]=='L':x-=1
        if s[i]=='R':x+=1
        if s[i]=='U':y+=1
        if s[i]=='D':y-=1

        try:
            if dic[x,y]:
                dic[x,y].append(i+1)
                temp = dic[x,y][-1]-dic[x,y][-2]
                if temp<least:
                    least = dic[x,y][-1]-dic[x,y][-2]
                    res = [dic[x,y][-2],dic[x,y][-1]]
        except KeyError:
            dic[x,y]=[i+1]

            
    if len(res)>1:
        print(res[0]+1,res[1])
    else:
        print(-1)

    
