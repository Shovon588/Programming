n,k=map(int,input().split())
s=input()
a=list(map(str,input().split()))

count=0;res=0
for i in range(n):
    if s[i] in a:
        count+=1
    else:
        res=res+((count*(count+1))//2)
        count=0

res=res+((count*(count+1))//2)
print(res)
        
