n,k = map(int,input().split())
a = list(map(int,input().split()))

b = set(a)
new=[];flag=-1;

if len(b)!=n:
    flag=0
else:
    for i in range(n):
        temp=a[i]&k
        if (temp!=a[i]) and (temp in a):
            flag=1
            
            break
        else:
            if temp not in new:
                new.append(temp)
            else:
                flag=2
                break

print(flag)
