n,m = map(int,input().split())

a = input()

a = ''.join(set(a))

a = list(a)
a.sort()

b = ord(a[0])
count=b-96
m-=1

if m>0:
    for i in range(1,len(a)):
        if ord(a[i])-b>=2:
            b=ord(a[i])
            count=count+(b-96)
            m-=1

            if m==0:
                break

if m>0:
    print(-1)
else:
    print(count)
