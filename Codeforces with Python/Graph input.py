k=int(input())
a=[[0 for i in range(k+1)]for j in range(k+1)]

for i in range(1,k+1):
    n,m,o=map(int,input().split())
    a[n][m]=o
    a[m][n]=o

for i in range(1,k+1):
    for j in range(1,k+1):
        print(a[i][j],end=' ')
    print()
