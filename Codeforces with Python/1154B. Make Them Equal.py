n=int(input())
a=list(map(int,input().split()))
b=set(a)

if len(b)==1:print(0)
elif len(b)==2:
     temp=max(a)+min(a)
     if temp%2==0:print(max(a)-(temp//2))
     else:print(max(a)-min(a))
else:
     flag=''
     temp=max(a)+min(a)
     if temp%2==0:
          temp1=max(a)-(temp//2)
          temp2=(max(a)-(temp//2))+min(a)
     for i in range(n):
          if a[i]+temp1==temp2 or a[i]==temp2 or a[i]-temp1==temp2:
               pass
          else:
               print(-1)
               flag='no'
               break

     if flag!='no':
          print(temp1)
