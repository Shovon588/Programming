n=int(input())

ina=0;inb=0;count=1

for i in range(n):
     a,b=map(int,input().split())

     #count+=max(0,min(a,b)-max(ina,inb)+int((ina!=inb)))
     temp1=max(0,min(a,b)-max(ina,inb)+int((ina!=inb)))
     temp2=max(0,min(a,b)-max(ina,inb))
     print(int((ina!=inb)))
     ina=a;inb=b

print(count)
