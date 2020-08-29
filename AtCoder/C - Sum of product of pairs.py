n = int(input())
a = list(map(int,input().split()))

cumsum = []
total = 0
for num in a:
    total+=num
    cumsum.append(total)

result = 0
MOD = pow(10,9)+7
for i,num in enumerate(cumsum):
    temp = total-num
    result += temp*a[i]
    
print(result%MOD)
    
