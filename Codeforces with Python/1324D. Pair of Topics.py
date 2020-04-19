n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort(reverse=True)
b.sort(reverse=True)

count=0
for i in range(n-1):
    mina = a[i]+a[-1]
    maxb = b[i]+b[i+1]

    if mina>maxb:
        count+=n-(i+1)
    elif mina==maxb:
        for j in range(i+2,n):
            if b[j]<b[i+1]:
                count+=n-j
                break
    else:
        for j in range(i+1,n):
            if b[i]+b[j]<mina:
                count+=n-j
                break
print(count)
