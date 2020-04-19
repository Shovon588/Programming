n=int(input())

temps=0
for i in range(n):
    x1,x2=map(int,input().split())
    temp=x1+x2
    if temp>temps:
        temps=temp

print(temps)
    
