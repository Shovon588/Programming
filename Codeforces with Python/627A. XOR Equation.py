s,x=map(int,input().split())

temp=s//2

count=0;check=0
for i in range(1,temp+1):
     if (i^(s-i))==x:
          if i!=s-i:
               count+=1
          else:
               check=1

print((2*count)+check)
