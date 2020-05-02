temp=[]
for i in range(1,31):
    temp.append(pow(2,i))

for _ in range(int(input())):
    n = int(input())
    half = n//2

    first = 0
    for i in range(half-1):
        first+=temp[i]
    first+=temp[n-1]

    second = 0
    for i in range(half-1,n-1):
        second+=temp[i]

    print(abs(first-second))
