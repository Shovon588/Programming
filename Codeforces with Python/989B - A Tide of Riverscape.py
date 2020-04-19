n,p=map(int,input().split())

a = input()

count=0
for i in range(n-p):
    if a[i]=='.' and a[i+p]=='.':
        x=i;y=i+p
        a = a[0:x].replace('.','0')+a[x].replace('.','1')+a[x+1:].replace('.','0')
        a = a[0:y].replace('.','1')+a[y].replace('.','0')+a[y+1:].replace('.','1')
        break
    elif (a[i]=='0' and a[i+p]=='.') or (a[i]=='.' and a[i+p]=='0'):
        a = a.replace('.','1')
        break
    elif (a[i]=='1' and a[i+p]=='.') or (a[i]=='.' and a[i+p]=='1'):
        a = a.replace('.','0')
        break
    else:
        count+=1


if count==n-p:
    print('No')
else:
    print(a)
