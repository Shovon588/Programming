s=input()
l=len(s)

check='123456789'
a=s.find('^')
left=0;right=0
for i in range(a):
    if s[i] in check:
        left+=(int(s[i])*abs(a-i))
for i in range(a,l):
    if s[i] in check:
        right+=(int(s[i])*abs(a-i))

if left==right:
    print('balance')
elif left>right:
    print('left')
else:
    print('right')
