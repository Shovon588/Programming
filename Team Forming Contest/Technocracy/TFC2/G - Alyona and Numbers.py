n,m=map(int,input().split())

count=0
for i in range(1,n+1):
     temp=i%5
     req=5-temp
     res=(m-req)//5
     count+=(res+1)

print(count)
          
     
