
n, x, y = map(int, input().split())
a = list(map(int, input().split()))
m = -1
k = 0
for i in range(n):
    if a[i] < m or m == -1:
        m = a[i]
        k = i
    if i-k >= y:
        break
print(k+1)
