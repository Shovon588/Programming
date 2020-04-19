n=int(input())
a=list(map(int,input().split()))

dic={}

for i in a:
     if i in dic:
          dic[i]+=1
     else:
          dic[i]=1
b=a[::]
b.sort()

for i in range(n):
     temp1=a[i]
     if b[0]==temp1 and dic[temp1]==1:
          temp2=b[1]
     else:temp2=b[0]
