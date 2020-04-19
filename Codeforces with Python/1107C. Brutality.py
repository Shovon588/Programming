n,k=map(int,input().split())
#a=list(map(int,input().split()))
#s=input()
a=[]
for i in range(1,10):
    a.append(i)
s='a'*9


sp=0;ep=0;temp=s[0];result=0;happened=False

for i in range(1,n):
    if s[i]==temp:
        ep+=1
    else:
        temp=s[i]
        flag=a[sp:ep+1]
        flag.sort(reverse=True)
        if ep-sp+1>k:
            result+=sum(flag[:k])
            sp=i;ep=i
        else:
            result+=sum(flag)
            sp=i;ep=i
        print(flag)
    if i==n-1:
        temp=a[sp:ep+1]
        temp.sort(reverse=True)
        result+=sum(temp[:k])

if n==1:
    print(a[0])
else:
    print(result)
