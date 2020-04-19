n,m = map(int,input().split())

a = list(map(int,input().split()))

b = []

for i in range(m):
    if a[i] not in b:
        b.append(a[i])

c =[]

for i in range(len(b)):
    c.append(a.count(b[i]))

c.sort()
b=c
c=c[::-1]

