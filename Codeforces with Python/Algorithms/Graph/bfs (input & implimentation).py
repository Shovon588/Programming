n,e = map(int,input().split())

vis=[False]*(n+1);
a=[[0 for i in range(e+2)]for j in range(e+2)]

for i in range(e):
    b,c=map(int,input().split())
    a[b][c]=1

b=[];z=[]
b.append(int(input()))

while(1):
    if len(b)>0:
        c=b[0]
        vis[c]=True
        
        for i in range(n+1):
            if a[c][i]==1 and vis[i]==False:
                b.append(i)
                vis[i]=True
        z.append(c)
        b.remove(c)
    else:
        break

print(z)
    
