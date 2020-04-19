s=input()

left=0;right=0
for i in range(len(s)):
    if s[i]==')':
        left=i+1
        break
for i in range(len(s)-1,-1,-1):
    if s[i]=='(':
        right=i+1
        break


total = left-1
total+=len(s)-right
if total==0:
    print(0)
else:
    print(total)

    for i in range(1,left):
        print(i,end=' ')
    for i in range(right+1,len(s)+1):
        print(i,end=' ')
