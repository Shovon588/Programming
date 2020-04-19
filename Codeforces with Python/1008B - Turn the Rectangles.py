n = int(input())

w = []; h = [];
for i in range(n):
    a,b = map(int,input().split())
    w.append(a)
    h.append(b)

if w[0]>=h[0]:
    high=w[0]
    low=h[0]
else:
    high=h[0]
    low=w[0]

a =[high]
code=0
for i in range(1,n):
    if w[i]>=h[i]:
        high=w[i]
        low=h[i]
    else:
        high=h[i]
        low=w[i]

    temp = a[len(a)-1]

    if high<=temp:
        a.append(high)
    elif low<=temp:
        a.append(low)
    else:
        code=1
        break
        
        
if code==1:
    print('NO')
elif code==0:
    print('YES')
