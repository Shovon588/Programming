dic = {1:'A',2:'B',3:'C'}

for i in range(int(input())):
    a=list(map(int,input().split()))

    maxa=max(a);mina=min(a)
    mida = sum(a)-maxa-mina
    
    if maxa==mida:
        print('Case %d: Confused' %(i+1))
    else:
        temp = a.index(maxa)+1
        print('Case %d: %s' %(i+1,dic[temp]))
