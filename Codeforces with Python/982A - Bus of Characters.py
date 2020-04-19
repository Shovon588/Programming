n=int(input())
a=list(map(int,input().split()))
b=input()

c=[[0 for i in range(2)]for j in range(n)]

for i in range(n):
    for j in range(2):
        if j==1:
            c[i][j]=i+1
        else:
            c[i][j]=a[i]
c.sort()
result=[];j=0;temp=[]

for i in range(2*n):
    if b[i]=='0':
        result.append(c[j][1])
        temp.append(c[j][1])
        j+=1
    else:
        z=temp.pop()
        result.append(z)
        
for x in range(len(result)):
    print(result[x],end=' ')
