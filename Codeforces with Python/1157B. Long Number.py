n=int(input())
s=list(input())
a=list(map(int,input().split()))


tempa=0;tempb=0
for i in range(n):
     temp=int(s[i])
     if temp<a[temp-1]:
          tempa=temp
          tempb=a[temp-1]
          break

if tempa==0 and tempb==0:
     print(''.join(s))
else:
     for i in s:
          if int(i)==tempa:
               print(tempb,end='')
          else:
               print(int(i),end='')
