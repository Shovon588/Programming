n = int(input())
a=[];count=0;
for i in range(n):
    a.append(input())

for i in range(n):
    try:a.remove(input())
    except:count+=1

print(count)
