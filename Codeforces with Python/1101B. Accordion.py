a=input()
lena=len(a)


yes=0
for i in range(lena):
    if a[i]=='[':
        l=i;yes+=1
        break

if yes==1:
    for i in range(lena-1,0,-1):
        if a[i]==']':
            r=i
            yes+=1
            break

if yes==2:
    a=a[l:r+1]
    lena=len(a)

    if a.count(':')==2:
        l=a.index(':')
        for i in range(lena-1,l,-1):
            if a[i]==':':
                r=i
                break
        count=0
        for i in range(l,r+1):
            print(a[i])
            if a[i]=='|':
                count+=1
        print(count+4)
    else:
        print(-1)
else:
    print(-1)
