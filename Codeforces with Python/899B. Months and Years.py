months=[31,28,31,30,31,30,31,31,30,31,30,31]*3
n=int(input())
a=list(map(int,input().split()))

if a.count(29)>1:
     print('No')
else:
     for i in range(n):
          if a[i]==29:
               a[i]=28

     flag='off'
     for i in range(36):
          if months[i:i+n]==a:
               print('Yes')
               flag='on'
               break
     if flag=='off':
          print('No')
