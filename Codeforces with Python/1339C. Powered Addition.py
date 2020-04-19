from sys import stdout,stdin

input=stdin.buffer.readline

def makeAList():
    last=0;arr = []
    for i in range(31):
        last=last+pow(2,i)
        arr.append(last)
    return arr

def findTheIndex(n):
    left=0;right=30

    while(abs(left-right)>1):
        mid = (left+right)//2
        if n>=l[left] and n<=l[mid]:
            right=mid
        else:
            left=mid
    
    if l[left]==n:
        return left
    else:
        return right    

l = makeAList()

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    maxi = 0
    for i in range(1,n):
        if a[i]<a[i-1]:
            temp = abs(a[i-1]-a[i])
            index = findTheIndex(temp)
            a[i] = a[i-1]
            maxi = max(maxi,index+1)

    stdout.write(str(maxi)+'\n')
