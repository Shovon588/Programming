l,r=map(int,input().split())


if l%2!=0:l+=1
if r-l>=2:
     print(l,l+1,l+2)
else:
     print(-1)
