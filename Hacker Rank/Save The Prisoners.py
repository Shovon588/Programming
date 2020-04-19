result = []
for _ in range(int(input())):
    n, c, k = map(int,input().split())
    rem = c%n

    if rem==0:
        if k==1:
            result.append(n)
        else:
            result.append(k-1)
    elif rem>n-k+1:
        rem = rem - (n-k+1)
        result.append(rem)
    else:
        result.append(rem+k-1)

    print(result[-1])

actual = []
for i in range(100):
    actual.append(int(input()))

for i in range(100):
    if result[i]!=actual[i]:
        print(result[i], actual[i], i)
    
