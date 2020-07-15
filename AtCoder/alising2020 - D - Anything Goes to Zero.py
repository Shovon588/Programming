n = int(input())
s = input()

def popcount(n):
    return bin(n).count('1')
    

to_add = 1
tot = 0
counta = 0
for i in range(n-1,-1,-1):
    if s[i]=='1':
        tot+=to_add
        counta += 1

    to_add = 2*to_add
    
to_add = to_add//2

for i in range(n):
    if s[i]=='1':
        temp = tot-to_add
        tempa = counta-1
    else:
        temp = tot+to_add
        tempa = counta+1
        
    temp = temp%tempa
    count = 1
    while temp>0:
        temp = temp%popcount(temp)
        count+=1
    print(count)
    
    to_add = to_add//2
    
