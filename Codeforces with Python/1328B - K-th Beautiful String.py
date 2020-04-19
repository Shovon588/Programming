def makeTheBase():
    base = []
    total = 1
    for i in range(1,63247):
        total+=i
        base.append(total)
    return base

def binSearch(num):
    left = 0
    right = 63247
    while(abs(left-right)>1):
        mid = (left+right)//2

        if num>=base[left] and num<=base[mid]:
            right = mid
        else:
            left=mid
            
    return left, right

def positionOfB(n,k):
    if k==1:
        b1 = n-2
        b2 = n-1
    else:
        left, right = binSearch(k)
        if base[right]==k:
            pos = right+1
        else:
            pos = left+1
            
        temp = base[pos-1]
        dif = abs(temp-k)
        
        b1 = abs(pos-(n-2))
        b2 = abs(dif-(n-1))

    return b1,b2

def printMe(n,pos1,pos2):
    for i in range(n):
        if i==pos1 or i==pos2:
            print('b',end='')
        else:
            print('a',end='')
    print()




base = makeTheBase()
for _ in range(int(input())):
    n, k = map(int,input().split())
    pos1, pos2 = positionOfB(n,k)
    printMe(n,pos1,pos2)
    







