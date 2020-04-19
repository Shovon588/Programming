n = int(input())
a = list(map(int,input().split()))


count=0
for i in range(n-1):
    if a[i]%2==0:
        continue
    else:
        a[i]+=1
        a[i+1]+=1
        count+=2

if a[-1]%2==1:
    print('NO')
else:
    print(count)
