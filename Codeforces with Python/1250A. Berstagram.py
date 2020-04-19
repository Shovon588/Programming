n,m=map(int,input().split())
a=list(map(int,input().split()))

check=[[i,i] for i in range(n+1)]
pos={};find=[i for i in range(n+1)]

for i in range(n):
    pos[i+1]=i+1

for i in a:
    temp1=pos[i] #position of i
    
    if temp1>1:
        temp2=find[temp1-1] #position of the element before i
        find[temp1],find[temp1-1]=temp2,i
        pos[temp2],pos[i]=temp1,temp1-1

        check[temp2][0]=max(check[temp2][0],temp1)
        check[temp2][1]=min(check[temp2][1],temp1)
        check[i][0]=max(check[i][0],temp1-1)
        check[i][1]=min(check[i][1],temp1-1)

for i in range(1,n+1):
    print(min(check[i][0],check[i][1]),max(check[i][0],check[i][1]))
    
