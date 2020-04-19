a = input()
flag = True

for i in range(len(a)-1):
    if a[i] not in 'aeioun' and a[i+1] not in 'aeiou':
        flag = False

if a[-1:] not in 'aeioun': flag = False

if flag:
    print('YES')
else:
    print('NO')
