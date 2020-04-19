data=[0 for i in range(202)]

def fun(x):
    if x==1:return 1

    if x%2==0:
        if data[x]==0:
            data[x]=(fun(x//2)*fun(x//2))+1

        return data[x]

    else:
        if data[x]==0:
            data[x]=(fun(x//2)*fun((x//2)+1))+2
        return data[x]

for i in range(1,46):
    fun(i)

data[1]=1

dic={}

for i in range(46):
    dic[data[i]]=i

for i in range(int(input())):
    n=int(input())
    print('Case %d: %d'%(i+1,dic[n]))
