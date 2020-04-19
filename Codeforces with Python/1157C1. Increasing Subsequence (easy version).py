n=int(input())
a=list(map(int,input().split()))
count=0;res=[];left=0;right=n-1;last=0

i=0
while(1):
     if a[left]>last and a[right]>last:
          if a[left]<a[right]:
               count+=1;res.append('L');last=a[left];left+=1
          else:
               count+=1;res.append('R');last=a[right];right-=1
     elif a[left]>last:
          count+=1;res.append('L');last=a[left];left+=1
     elif a[right]>last:
          count+=1;res.append('R');last=a[right];right-=1
     else:
          break
     i+=1
     if i==n:break
                                   
print(count)
print(''.join(res))
