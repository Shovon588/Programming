n, k , q = map(int,input().split())
a = list(map(int,input().split()))

for i in range(q):
    x = int(input())
    x -= k

    if x<0:
        x += n

    print(a[x])
