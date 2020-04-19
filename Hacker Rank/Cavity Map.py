import re

n = int(input())

mat = []

for i in range(n):
    s = input()
    s = re.findall('.', s)
    mat.append(s)


pos = []
for i in range(1,n-1):
    for j in range(1,n-1):
        num = int(mat[i][j])
        up = int(mat[i][j+1])
        down = int(mat[i][j-1])
        left = int(mat[i-1][j])
        right = int(mat[i+1][j])

        if num>up and num>down and num>left and num>right:
            pos.append((i,j))


for left,right in pos:
    mat[left][right]='X'

res = []
for i in range(n):
    temp = ''.join(mat[i])
    res.append(temp)
