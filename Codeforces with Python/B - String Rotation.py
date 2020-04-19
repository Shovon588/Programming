a=input()
b=input()

flag=0
if a==b:
    flag=1
else:
    for i in range(len(a)):
        a=a[-1:]+a[:-1]
        if a==b:
            flag=1
            break

if flag==1:
    print('Yes')
elif flag==0:
    print('No')
