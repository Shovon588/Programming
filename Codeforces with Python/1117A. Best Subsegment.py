n=int(input())
a=list(map(int,input().split()))

maxa=max(a)


total=0;res=0;count=0
for i in range(n):
     total+=a[i]
     count+=1

     
     if total/count==maxa:
          if count>res:
               res=count
          continue
     else:
          total=0;count=0
          
     
print(res)
