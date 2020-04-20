v,e=map(int,input().split())
vis=[False]*(v+1)
a=[[10000 for i in range(v+1)] for j in range(v+1)]
z=[]


for i in range(e):
    b,c=map(int,input().split())
    a[b][c]=1

    
b=[0];z=[]

while(1):
    if len(b)>0:
        c=b[0]
        vis[c]=True
        for i in range(v):
            if a[c][i]==1 and vis[i]==False:
                a[c][i]=i
                vis[i]=True
                b.append(i)
        z.append(c)
        b.remove(c)
        
    else:
        break

#b=int(input())
