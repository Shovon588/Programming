n=int(input())
a=list(map(int,input().split()))

while(1):
     m=n//2
     left=1;right=1;lmax=0;rmax=0

     for i in range(m-1):
          if a[i]>=a[i-1]:
               left+=1
               if left>lmax:lmax=left
          else:
               left=1
          

     for i in range(m,n):
          if a[i]>=a[i-1]:
               right+=1
               if right>rmax:rmax=right
          else:
               right=1

     print(a[:m])
     print(a[m:])

     if lmax+rmax==n:
          print(lmax+rmax)
          break

     (lmax,rmax)

     if lmax>=rmax:
          a=a[:m]
          n=n//2
     else:
          a=a[m:]
          n=n//2
     
