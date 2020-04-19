s = input()
t = input()
k = int(input())

ls = len(s)
lt = len(t)

for i in range(min(ls,lt)):
    if s[i]!=t[i]:
        i-=1
        break

if i==lt-1:
    rem = ls-i-1
else:
    rem = ls-i-1
    rem += lt-i-1

if rem<=k:
    print('Yes')
else:
    print('No')
