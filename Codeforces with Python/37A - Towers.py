n = int(input())

a = list(map(int,input().split()))
b = a.count(max(set(a), key=a.count))
c=[]

for i in range(n):
    if a[i] in c:
        n-=1
    else:
        c.append(a[i])

print(b,n)
