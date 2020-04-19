n = int(input())

data=[]
for i in range(n):
    a,b,c,d = map(int,input().split())
    data.append(a+b+c+d)

check=data[0];count=1;

for i in range(1,n):
    if data[i]>check:
        count+=1

print(count)
