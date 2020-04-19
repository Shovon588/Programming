a={}
for i in range (int(input())):
    p,q = map(int,input().split())
    a[p]=q

for i in range(int(input())):
    p,q = map(int,input().split())

    if p in a and a[p]<q:
        a[p]=q
    elif p not in a:
        a[p]=q

print (sum(a.values()))
