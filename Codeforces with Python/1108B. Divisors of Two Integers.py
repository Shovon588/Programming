n=int(input())
a=list(map(int,input().split()))

temp=max(a)

first=[];second=[]
for i in a:
    if temp%i==0 and i not in first:
        first.append(i)
    else:
        second.append(i)
print(max(first),max(second))
