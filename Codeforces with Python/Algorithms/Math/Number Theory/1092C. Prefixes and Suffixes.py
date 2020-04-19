n=int(input())
a=[];z=''
for _ in range(2*n-2):
    y=input()
    z+=y
    a.append(y)

z=''.join(set(z))

b=[];temp=''
for i in range(2*n-2):
    for j in range(2*n-2):
        if i!=j:
            temp=a[i]+a[j]

        if len(temp)==n:
             b.append(temp)

count=0
for i in range(len(b)):
    if ''.join(set(b[i]))==z:
        temp=b.count(b[i])
        if temp>count:
            count=temp
            flag=b[i]

rep=[];result=''
for i in range(2*n-2):
    temp=a[i]
    if flag.index(temp)==0 and temp not in rep:
        result+='P'
        rep.append(temp)
    else:
        result+='S'

print(result)
