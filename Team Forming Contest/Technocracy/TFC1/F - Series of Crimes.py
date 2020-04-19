n,m=map(int,input().split())

k=0;b=[]
for i in range(n):
     s=input()
     for j in range(m):
          if s[j]=='*':
               b.append((i+1,j+1))
               k+=1

x1,y1=b[0][0],b[0][1]
x2,y2=b[1][0],b[1][1]
x3,y3=b[2][0],b[2][1]


if x1==x2:
     x4=x3

     if y3==y1:
          y4=y2
     elif y3==y2:
          y4=y1
     
elif x1==x3:
     x4=x2

     if y2==y1:
          y4=y3
     elif y2==y3:
          y4=y1
          
elif x2==x3:
     x4=x1

     if y1==y2:
          y4=y3
     elif y1==y3:
          y4=y2
print(x4,y4)
