from sys import stdout,stdin
 
#input=stdin.buffer.readline

n,m,k = map(int,input().split())

alice = [(0,0)]
bob = [(0,0)]
common = [(0,0)]
none = [(0,0)]

la = 1
lb = 1
lc = 1

for i in range(n):
    t,a,b = map(int,input().split())
    if a==1 and b==1:
        common.append((t,i+1))
        lc+=1
    elif a==1 and b==0:
        alice.append((t,i+1))
        la+=1
    elif b==1 and a==0:
        bob.append((t,i+1))
        lb+=1
    else:
        none.append((t,i+1))

alice.sort()
bob.sort()
common.sort()

alicecum = []
bobcum = []
commoncum = []

tot = 0
for num in alice:
    tot+=num[0]
    alicecum.append(tot)
    
tot = 0
for num in bob:
    tot+=num[0]
    bobcum.append(tot)

tot = 0
for num in common:
    tot+=num[0]
    commoncum.append(tot)

p1 = min(k,lc-1)
p2 = k-p1

if 2*k-p1>m or p2>min(la-1,lb-1):
    stdout.write(str(-1)+'\n')
else:
    res = 100000000000000055
    fromal = 0
    frombo = 0
    fromco = 0
    total = 0
    for i in range(k+1):
        com = k-i
        al, bo = i, i
        
        if com<lc and al<la and bo<lb:
            temp = commoncum[com]
            temp += alicecum[al]
            temp += bobcum[bo]
            tot = al+com+bo
            
            if temp<res and tot<=m:
                res = temp
                total = tot
                fromal = al
                frombo = bo
                fromco = com
    unused = []
    resarr = []
    for i in range(1,len(alice)):
        if i<=fromal:
            resarr.append(alice[i][1])
        else:
            unused.append(alice[i])
        
    for i in range(1,len(bob)):
        if i<=frombo:
            resarr.append(bob[i][1])
        else:
            unused.append(bob[i])

    for i in range(1,len(common)):
        if i<=fromco:
            resarr.append(common[i][1])
        else:
            unused.append(common[i])

    for i in range(1,len(none)):
        unused.append(none[i])
        
    unused.sort()
    for i in range(m-total):
        res+=unused[i][0]
        resarr.append(unused[i][1])
    
    stdout.write(str(res)+'\n')
    print(*resarr)

