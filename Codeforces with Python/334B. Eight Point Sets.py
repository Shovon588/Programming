first=[];second=[]

for i in range(8):
    x,y=map(int,input().split())
    first.append(x)
    second.append(y)

x=[];y=[]

for i in first:
    if i not in x:
        x.append(i)

for i in second:
    if i not in y:
        y.append(i)
