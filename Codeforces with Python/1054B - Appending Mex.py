n=int(input())
a=list(map(int,input().split()))

initial=0;problem=False
for i in range(n):
    if a[i]==initial:
        initial+=1
    elif a[i]<initial:
        continue
    else:
        problem=True
        break

if problem==True:print(i+1)
else:print(-1)
