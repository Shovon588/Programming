n = int(input())

a = list(map(int,input().split()))

count = 0
b =[]
for i in range(n):
    if a[i]==1 and i!=0:
        b.append(a[i-1])
        count+=1
    

b.append(a[n-1])

print(count+1)
for i in range(len(b)):
    print(b[i],end=' ')
