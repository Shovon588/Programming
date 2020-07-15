from sys import stdout,stdin
 
input=stdin.buffer.readline

n,k = map(int,input().split())

alice = [0]
bob = [0]
common = [0]
la = 1
lb = 1
lc = 1
for i in range(n):
    t,a,b = map(int,input().split())
    if a==1 and b==1:
        common.append(t)
        lc+=1
    elif a==1:
        alice.append(t)
        la+=1
    elif b==1:
        bob.append(t)
        lb+=1

alice.sort()
bob.sort()
common.sort()

alicecum = []
bobcum = []
commoncum = []

tot = 0
for num in alice:
    tot+=num
    alicecum.append(tot)
    
tot = 0
for num in bob:
    tot+=num
    bobcum.append(tot)
tot = 0
for num in common:
    tot+=num
    commoncum.append(tot)

if la+lc-2<k or lb+lc-2<k:
    stdout.write(str(-1)+'\n')
else:
    res = 100000000000055
    for i in range(k+1):
        com = k-i
        al, bo = i, i
        
        if com<lc and al<la and bo<lb:
            temp = commoncum[com]
            temp += alicecum[al]
            temp += bobcum[bo]
            res = min(res,temp)


    stdout.write(str(res)+'\n')

