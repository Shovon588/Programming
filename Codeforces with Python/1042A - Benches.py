n=int(input())
m=int(input())

a=[];b=m;
for i in range(n):
    a.append(int(input()))
a.sort()
maxa=max(a)

for i in range(n):
    if a[i]<maxa:
        if m>=maxa-a[i]:
            m=m-(maxa-a[i])
            a[i]+=maxa-a[i]
        else:
            a[i]+=m
            m=0
    if m==0:
        break

temp=max(a)

temp+=m//n

if m%n!=0:
    temp+=1

print(temp,maxa+b)
