red, green, blue = map(int,input().split())
r = list(map(int,input().split()))
g = list(map(int,input().split()))
b = list(map(int,input().split()))

maxi = max(max(red,green),blue)
mini = min(min(red,green),blue)
mid = (red+green+blue)-(maxi+mini)

iteration = min(maxi,mini+mid)

print(iteration)

r.sort(reverse=True)
g.sort(reverse=True)
b.sort(reverse=True)

ri=0
gi=0
bi=0

res = 0
while iteration>0:
    maxi=0
    maxifrom = ''
    if ri<red:
        if max(maxi,r[ri])>maxi:
            maxi = max(maxi,r[ri])
            maxifrom='r'
        
    if gi<green:
        if max(maxi,g[gi])>maxi:
            maxi = max(maxi,g[gi])
            maxifrom='g'
    if bi<blue:
        if max(maxi,b[bi])>maxi:
            maxi = max(maxi,b[bi])
            maxifrom='b'

    mini = 100000
    minfrom = ''
    if ri<red:
        if min(mini,r[ri])<mini:
            mini = min(mini,r[ri])
            minfrom='r'
    if gi<green:
        if min(mini,g[gi])<mini:
            mini = min(mini,g[gi])
            minfrom='g'
    if bi<blue:
        if min(mini,b[bi])<mini:
            mini = min(mini,b[bi])
            minfrom='b'


    try:
        mid = (r[ri]+g[gi]+b[bi])-(maxi+mini)
        for char in 'rgb':
            if char!=maxifrom and char!=minfrom:
                midfrom=char
    except IndexError:
        mid = mini
        midfrom = minfrom

    
    if maxifrom=='r' and midfrom=='g':
        res+= r[ri]*g[gi]
        ri+=1
        gi+=1
    elif maxifrom=='r' and midfrom=='b':
        res+= r[ri]*b[bi]
        ri+=1
        bi+=1
    elif maxifrom=='g' and midfrom=='r':
        res+= g[gi]*r[ri]
        gi+=1
        ri+=1
    elif maxifrom=='g' and midfrom=='b':
        res+= g[gi]*b[bi]
        gi+=1
        bi+=1
    elif maxifrom=='b' and midfrom=='r':
        res+= b[bi]*r[ri]
        bi+=1
        ri+=1
    elif maxifrom=='b' and midfrom=='g':
        res+= b[bi]*g[gi]
        bi+=1
        gi+=1
        
    iteration-=1
    print(maxi,maxifrom,mid,midfrom)
    
print(res)


    
