n = int(input())

a = list(map(int,input().split()))

b = sum(a)

sum1 = []; sum2 = [];
c=0;d=0;

j = n-1

flag=0
if n==1:
    flag=1
else:
    for i in range(n):
        
        c+=a[i]
        sum1.append(c)

        d+=a[j]
        sum2.append(d)
        j-=1

        if c+a[i+1]>b//2 and d+a[j]>b//2:
            break


if flag==1:
    print(0)
else:
    if len(set(sum1) & set(sum2))==0:
        print(0)
    else:
        print(max(set(sum1) & set(sum2)))
