sums = []
count=0
for i in range(1,6330,2):
    sums.append(count)
    if count>=10000005:
        break
    count+=i


for _ in range(int(input())):
    n,k = map(int,input().split())

    if k>3163:
        temp = n-sums[-1]
    else:
        temp = n-sums[k-1]
    
    if temp%2==1 and temp>((k-1)*2)-1:
        print('YES')
    else:
        print('NO')
