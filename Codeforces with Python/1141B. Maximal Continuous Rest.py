n=int(input())
a=list(map(int,input().split()))

count=[];flag=0
for i in range(n):
     if a[i]==1:
          flag+=1
     else:
          count.append(flag)
          flag=0

for i in range(n):
     if a[i]==1:
          flag+=1
     else:
          break
count.append(flag)
print(max(count))
