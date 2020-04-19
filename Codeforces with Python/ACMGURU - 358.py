b=[]
for i in range(3):
    a=list(map(int,input().split()))

    a.sort()
    b.append(a[1])

b.sort()
print (b[1])

