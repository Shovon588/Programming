t=int(input())
for _ in range(t):
    v,e=map(int,input().split())
    a=[[0 for i in range (v)]for j in range(v)]

    for i in range(e):
        x,y=map(int,input().split())
        a[x][y]=1
        a[y][x]=1

    for i in range(v):
        print(i,end='')
        for j in range(v):
            if a[i][j]==1:
                print('->',j,end='')
                
        print()
