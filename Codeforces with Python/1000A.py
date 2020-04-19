n=int(input())
a=[]
b=[]
for i in range(n):
    temp=input()
    a.append(temp)


for i in range(n):
    temp=input()
    b.append(temp)

c=set(a).intersection(b)

print(n-len(c))
