k=int(input())

i=10;count=0
while(k):
     i+=9
     if sum(map(int,str(i)))==10:
          k-=1
print(i)
