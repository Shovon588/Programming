from collections import Counter
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=Counter(a)

number=[];count=[]
for i in b:
    number.append(i)
    count.append(b[i])

possi=count[m-1]
