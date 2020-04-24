arr = []
tot = 1
for i in range(1,31):
    temp=pow(2,i)
    tot+=temp
    arr.append(tot)


for _ in range(int(input())):
    n = int(input())
    for i in range(n):
        if n%arr[i]==0:
            print(n//arr[i])
            break
