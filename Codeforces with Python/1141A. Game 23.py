n,m=map(int,input().split())

count=0
if m%n==0:
     m=m//n
     while m%2==0:
          m=m//2;count+=1
     while m%3==0:
          m=m//3;count+=1

     if m==1:print(count)
     else:print(-1)
else:
     print(-1)
