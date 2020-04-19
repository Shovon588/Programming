n,m=map(int,input().split())

a=list(map(int,input().split()))
a.sort(reverse=True)
b=a[::-1]
suma=sum(a)

j=0;count=0;total=0;i=0;k=0
check=[]

if suma<m:
     print(-1)
else:
     while(1):
          temp=a[i]-j
          j+=1
          

          if temp<=0:
               j=0;count+=1;i-=1
          else:
               check.append(temp)
               total+=temp
               m-=temp
               if m<=0:
                    count+=1
                    break
          i+=1
          if i==n:
               count+=1
               while m>0:
                    m-=check.pop()
                    m-=b[k]
                    k+=1;count+=1
               break
          
          
     print(count)
