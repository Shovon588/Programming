n = int(input())
b = bin(n)[2:]

res = n
for i in range(len(b)):
    b = b[1:]+b[0]
    res = max(res,int(b,2))
print(res)
