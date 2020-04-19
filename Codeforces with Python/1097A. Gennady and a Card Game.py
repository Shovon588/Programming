a=input()
b=list(map(str,input().split()))

x,y=a[0],a[1]

flag=0
for i in b:
    if x in i or y in i:
        flag=1
        break

if flag==1:print('YES')
else:print('NO')
