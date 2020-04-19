v,e=map(int,input().split())
vis=[False]*(v+1)

a=[[0 for i in range(v+1)] for j in range(v+1)]

for i in range(e):
    b,c=map(int,input().split())
    a[b][c]=1
    a[c][b]=1

for i in range(1,v+1):
    print(i,'->',end=' ')
    for j in range(v):
        if a[i][j]==1:
            print(j,end=' ')
    print()
