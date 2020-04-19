from math import sqrt as s

n=int(input())
a=list(map(int,input().split()))

a.sort()

maxa=a[-1];total=0;
for i in a:
    if i>0:
        mina=i
        break

for i in range(n):
    total+=maxa-a[i]


check=[]

for i in range(1,int(s(mina))+1):
    if mina%i==0:
        if i!=1:
            check.append(i)
        check.append(mina//i)
check.sort(reverse=True)

if n==2:
    print(1,total)
else:
    for i in check:
        if total%i==0:
            print(total//i,i)
            break
