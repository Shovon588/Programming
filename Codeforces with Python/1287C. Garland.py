n = int(input())
a = list(map(int,input().split()))

present = []; even = []; odd = []
temp = [0 for i in range(n+1)]

for i in range(n):
    if a[i]!=0:
        present.append(i)
        temp[a[i]]=1


for i in range(1,n+1):
    if temp[i]!=1:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
            
print(even)
print(odd)

if len(present)==0:
    a[0]=1
    present.append(0)
    odd.remove(1)

for i in present:
    if a[i]%2==0:
        if i!=0:
            if a[i-1]==0:
                present.append(i-1)
                if len(even)>0:
                    a[i-1]=even.pop()
                else:
                    a[i-1]=odd.pop()
        if i!=n-1:
            if a[i+1]==0:
                present.append(i+1)
                if len(even)>0:
                    a[i+1]=even.pop()
                else:
                    a[i+1]=odd.pop()
    
    else:
        if i!=0:
            if a[i-1]==0:
                present.append(i-1)
                if len(odd)>0:
                    a[i-1]=odd.pop()
                else:
                    a[i-1]=even.pop()
        if i!=n-1:
            if a[i+1]==0:
                present.append(i+1)
                if len(odd)>0:
                    a[i+1]=odd.pop()
                else:
                    a[i+1]=even.pop()

    
count=0
for i in range(n-1):
    if (a[i]%2==0 and a[i+1]%2==1) or (a[i]%2==1 and a[i+1]%2==0):
        count+=1

print(count)
