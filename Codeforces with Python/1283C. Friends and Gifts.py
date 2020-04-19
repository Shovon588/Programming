n=int(input())
a=list(map(int,input().split()))


temp = [0 for i in range(n+1)]
ovaga = []; bolod = []

for i in range(n):
    if a[i]!=0:
        temp[a[i]]+=1
    else:
        bolod.append(i+1)


for i in range(1,n+1):
    if temp[i]==0:
        ovaga.append(i)

left=0;right=len(ovaga)-1

last = []
for i in range(n):
    if a[i]==0:
        temp = ovaga[right]
        if temp==i+1:
            if right==left:
                flag=last[-1]
                temp1=flag[0]
                j=flag[1]

                a[j]=temp
                a[i]=temp1
                break
            else:
                temp=ovaga[left]
                left+=1
                last.append((temp,i))
        else:
            right-=1
            last.append((temp,i))
        a[i]=temp

print(*a)
