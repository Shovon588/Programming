n=int(input())
a=list(map(int,input().split()))

arr=[]
for i in range(n):
    arr.append((a[i],i+1))
    
arr.sort(reverse=True)

count=0

for i in range(n):
    count+=((i*arr[i][0])+1)
print(count)
for i in range(n):
    print(arr[i][1],end=' ')
