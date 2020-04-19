n,v=map(int,input().split())

if v>=n:
     print(n-1)
else:
     total=n-1-v
     tk=v
     for i in range(2,n+1):
          if total<=0:
               break
          tk+=i
          total-=1
     print(tk)
