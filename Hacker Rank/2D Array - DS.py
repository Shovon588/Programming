arr = []

for I in range(6):
    a = list(map(int,input().split()))
    arr.append(a)


maxi = -100002161515
for j in range(6):
    for i in range(6):
        if i!=0 and i!=5 and j!=0 and j!=5:
            num = arr[i-1][j-1]+arr[i-1][j]+arr[i-1][j+1]+arr[i][j]+arr[i+1][j-1]+arr[i+1][j]+arr[i+1][j+1]
            maxi = max(maxi,num)
print(maxi)
