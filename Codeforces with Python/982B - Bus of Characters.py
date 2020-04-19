n=int(input())
a=list(map(int,input().split()))
c=input()
l=len(c)

b=[]
for i in range(l):
    if c[i]=='0':
        index=a.index(min(a))
        a[index]=100000000000
        print(index+1,end=" ")
        b.append(index+1)
    else:
        print(b.pop(),end=" ")
    
