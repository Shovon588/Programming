s=input()

count=0;pos=0

for i in s:
    if i=='R':
        pos+=1
    else:
        pos-=1

    if pos==4:
        count+=1
        pos=0
    elif pos==-4:
        pos=0

print(count)
