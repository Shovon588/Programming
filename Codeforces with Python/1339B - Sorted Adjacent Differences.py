from sys import stdin, stdout

input = stdin.buffer.readline

t= int(input())

for _ in range(t):
    n = int(input())
    a = sorted(list(map(int,input().split())))

    ans = []
    for i in range(n//2):
        ans.append(a[i])
        ans.append(a[n-1-i])
    if n%2==1:
        ans.append(a[n//2])

    print(*ans[::-1])
