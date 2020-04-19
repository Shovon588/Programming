n=int(input())
a=list(map(int,input().split()))

total=0;big=0;small=105

for i in range(n):
     total+=a[i]
     if a[i]>big and a[i]%2==0:
          big=a[i]
     if a[i]<small:
          small=a[i]


for i in range(2,(big//2)+1):
     if big%i==0:
          temp=total-(big//i)
          temp=temp-small+(small*i)
     total=min(total,temp)

print(total)
