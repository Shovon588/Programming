n=int(input())
a=list(map(int,input().split()))

pos=0;neg=0
for i in range(n):
     if a[i]>0:pos+=1
     if a[i]<0:neg+=1

if n%2==0:check=n//2
else:check=(n//2)+1

if pos>=check:
     print(1)
elif neg>=check:
     print(-1)
else:
     print(0)
