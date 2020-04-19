n=int(input())
data=[]
for i in range(n):
     a,b=map(int,input().split())
     data.append((a,b))
data.sort(reverse=True)

res=0
for i in range(n):
     res+=(data[i][0]*(i+1-1))+(data[i][1]*(n-i+1))
     print(res)
     
