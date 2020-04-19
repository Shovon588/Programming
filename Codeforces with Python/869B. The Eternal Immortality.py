a,b=map(int,input().split())

two=0;five=0;res=1
for i in range(a+1,b+1):
    if i%2==0:
        two+=1
    elif i%5==0:
        five+=1

    if two>0 and five>0:
        res=0
        break
    res=res*i

res=str(res)
print(res[-1])
