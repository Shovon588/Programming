n=int(input())
s=input()

res=[0]*10

left=[0];right=[9]

for i in s:
    if i=='L':
        temp=left[-1]
        res[temp]=1

        if len(left)==1:
            left.pop()
            left.append(temp+1)
        else:
            left.pop()
    elif i=='R':
        temp=right[-1]
        res[temp]=1
        if len(right)==1:
            right.pop()
            right.append(temp-1)
        else:
            right.pop()
    else:
        temp=int(i)
        res[temp]=0

        if left[-1]>temp:
            left.append(temp)
        elif right[-1]<temp:
            right.append(temp)
    
for i in res:
    print(i,end='')
