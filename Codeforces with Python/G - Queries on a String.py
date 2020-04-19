s=input()
n=int(input())
p=''
x=[];y=[]


def sub(a,b):
    pos=0
    for ch in a:
        if pos<len(b) and ch==b[pos]:
            pos+=1
    return pos==len(b)

for i in range(n):
    i=j=0
    a=input()
    try:
        c,b=a.split()
    except ValueError:
        c=a

    if c=='push':
        p=p+b
    else:
        p=p[:len(p)-1]

    if p in x:
        ind=x.index(p)
        y.append(y[ind])
        x.append(p)
    else:
        temp=sub(s,p)

        if temp==True:
            x.append(p)
            temp.append('YES')
        else:
            x.append(p)
            temp.append('NO')
        
for i in range(n):
    print(temp[i])
