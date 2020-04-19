a=input()
b=input()

while (1):
    if a=='':
        break
    a=a.replace(a[0],'')
    b=b.replace(b[0],'')    

    if len(a)!=len(b):
        print('No')
        exit()

print('Yes')
