h,n=map(int,input().split())
a=list(map(int,input().split()))
suma=sum(a)

x=0;mina=100000000000
for i in a:
     x+=i
     if x<mina:mina=x

if suma>0 or abs(mina)<h:
     print(-1)
else:
     count=0;
     try:
          temp=h//abs(suma)
     except:
          temp=0

     if temp>4:
          h+=(temp-2)*suma
          count+=temp-2

     while h>abs(mina):
          h+=suma
          count+=1
     count=count*n
     
     for i in range(n):
          h+=a[i];count+=1
          if h<=0:break
     print(count)
