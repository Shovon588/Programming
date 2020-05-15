from math import ceil

for _ in range(int(input())):
    n,k = map(int,input().split())

    temp = ceil(k/(n-1))-1
    
    temp1 = temp*n
    temp2 = temp*(n-1)

    print(temp1+(k-temp2))
