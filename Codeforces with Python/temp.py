n = int(input())
a = list(map(int,input().split()))
p = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

dic = {}
for i in range(n):
    try:
        if dic[a[i]]:
            dic[a[i]].append(i)
    except KeyError:
        dic[a[i]]=[i]


def is_possible():
    last = -1
    for num in b:
        flag='ok'
        temp = dic[num]
        for x in temp:
            if x>last:
                last=x
                break
            
        if flag=='':
            return False
        
    return True


store = {}
if is_possible():
    for i in range(m):
        num = b[i]
        temp = dic[num]
        if len(temp)==1:
            store[num]=temp[0]
        else:

            if i!=m-1:
                check = dic[b[i+1]][0]
            else:
                check=dic[b[i]][-1]
                          
            for j in range(len(temp)):
                if temp[j]>check:
                    break
                
            store[num]=temp[j-1]

    for i in range(m):
        num = b[i]
        temp = dic[num]
        check = store[num]

        if i!=m-1:
            nextcheck = store[b[i+1]]

        for j in range(len(temp)):
            if temp[j]<nextcheck:
                store[num]=temp[j]
    
    left=0; total=0
    
    for i in range(1,m):
        bag = {}
        num = b[i-1]
        right = store[num]
            
        for j in range(left,right+1):
            if a[j]>num:
                total+=p[j]
                print(a[j],p[j],num, total)
            elif i==1 and a[j]<num:
                total+=p[j]
                print(a[j],p[j],num, total)
            elif a[j]==num:
                try:
                    if bag[num]:
                        bag[num].append(p[j])
                except KeyError:
                    bag[num]=[p[j]]
        
        for x in bag:
            total+=sum(bag[x])-max(bag[x])
            print(x,sum(bag[x])-max(bag[x]), total)

        left=right+1

    
    bag={}
    num=b[-1]
    
    for i in range(left,n):
        print(a[i])
        if a[i]>num:
            total+=p[i]
            print(a[i],p[i],total)

    print(total)
else:
    print('NO')




