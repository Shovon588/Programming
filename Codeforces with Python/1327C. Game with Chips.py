n,m,k = map(int,input().split())

cor = []

for i in range(k):
    x,y = map(int,input().split())

for i in range(k):
    x,y = map(int,input().split())


result = (n-1)*'U'
result += (m-1)*'L'

for i in range(n):
    if i%2==0:
        result += (m-1)*'R'
        result += 'D'
    else:
        result += (m-1)*'L'
        if i!=n-1:
            result += 'D'

print(len(result))
print(result)
