n=int(input())
a=list(map(int,input().split()))

cum=[0]*n;even=[0]*n;odd=[0]*n
cum[0]=a[0];odd[0]=a[0];even[0]=0

for i in range(1,n):
     cum[i]=cum[i-1]+a[i]
     
     if i%2!=0:
          even[i]=even[i-1]+a[i]
          odd[i]=odd[i-1]
     else:
          odd[i]=odd[i-1]+a[i]
          even[i]=even[i-1]
          

temp1=0;temp2=0;Etemp=0;Otemp=0;count=0
for i in range(n):
     if (i+1)%2==1:
          temp1=odd[i]-a[i]
          temp2=even[i]

     if (i+1)%2==0:
          temp2=even[i]-a[i]
          temp1=odd[i]

     Etemp=even[n-1]-even[i]
     Otemp=odd[n-1]-odd[i]

     if temp1+Etemp==temp2+Otemp:
          count+=1
print(count)
