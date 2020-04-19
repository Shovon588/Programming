n=int(input())

for i in range(n):
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    a=a[1:]
    b=b[1:]
    c=a+b
    c.sort()
    print(c)
