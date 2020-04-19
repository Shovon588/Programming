n,x=map(int,input().split())
a=list(map(int,input().split()))

b=list(range(x+1))
count=0
for i in b:
    if i not in a and i!=x:
        count+=1
    if i in a and i==x:
        count+=1

print(count)
