x,y,h,w,n=map(int,input().split())
a=list(map(int,input().split()))
a.sort(reverse=True)


height=x-h;width=y-w

if height<0:height=0
if width<0:width=0


i=0
while(1):
     if height<=0 and width<=0:
          break
     print(height,width)

     if height>=width:
          height=height-a[i]
          i+=1
     else:
          width=width-a[i]
          i+=1



print(i)
