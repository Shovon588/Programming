a = ['purple','green','blue','orange','red','yellow']
b = ['Power','Time','Space','Soul','Reality','Mind']
result=[]

for i in range(int(input())):
    c = input()
    if c in a:
        result.append(b[a.index(c)])

b = set(b)-set(result)
b=list(b)

if(len(b)>0):
    print(len(b))
    for i in range(len(b)):
        print (b[i],sep='\n')
else:
    print(len(b))
