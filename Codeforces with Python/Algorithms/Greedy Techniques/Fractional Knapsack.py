n=int(input()) #n= number of items
a=[];b=[]
for i in range(n):
     x,y=map(int,input().split()) #x=value of items...y=quantity items
     a.append((x,y))
     b.append((x/y,i)) #x/y is the value per unit item
     
b.sort(reverse=True)

w=int(input()) #w=total quantity to pick optimally

count=0
for i in range(n):
     temp=b[i][1]

     if a[temp][1]<=w:
          count+=a[temp][0]
          w-=a[temp][1]
     else:
          count+=(w*b[i][0])
          w=0
          
print(count) #count is the maximum amount possible to pick among the items
