n=int(input())

def Fact_N(n):
    a=[0 for i in range(n+1)]
    a[0]=1
    for i in range(1,n+1):
        a[i]=a[i-1]*i
    return a[-1]


a=Fact_N(n)
a=str(a)

if len(a)>4:
    print(a[len(a)-4:])
else:
    print(a)
