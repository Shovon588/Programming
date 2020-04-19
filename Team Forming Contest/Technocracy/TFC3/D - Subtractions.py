n=int(input())

for i in range(n):
     a,b=map(int,input().split())

     res=0

     while(1):
          if a>b and b!=0:
               res=res+(a//b)
               a=a%b
          elif a<b and a!=0:
               res=res+(b//a)
               b=b%a
          elif a==b and a!=0:
               res+=1
               break
          else:
               break

     print(res)
          
