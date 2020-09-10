n,m = map(int,input().split())

stars = []
for I in range(n):
    s = input()
    for i in range(m):
        if s[i]=='*':
            stars.append((I+1,i+1))

if stars[0][0]==stars[1][0]:
    if stars[0][1]==stars[2][1]:
        right = stars[1][1]
    else:
        right=stars[0][1]
        
    left = stars[2][0]
else:
    if stars[0][1]==stars[1][1]:
        right = stars[2][1]
    else:
        right=stars[1][1]
        
    left = stars[0][0]

print(left,right)
    
