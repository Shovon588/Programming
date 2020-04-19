a=input()
b=input()

h1=a[:2];h2=b[:2]
m1=a[3:];m2=b[3:]

if h1>h2:
     total=60-int(m1)+int(m2)+(24-(int(h1))-int(h2))*60
elif h1==h2:
     total=abs(int(m1)-int(m2))
else:
     total=60-int(m1)+int(m2)+abs((int(h1)+1-int(h2)))*60





total=total//2
h1=int(h1)
m1=int(m1)

m1+=total

if m1>=60:
     h1=h1+m1//60
     m1=m1%60

if h1>=24:
     h1=(h1-24)+1

if len(str(h1))==1:
     print('0'+str(h1)+':',end='')
else:
     print(str(h1)+':',end='')

if len(str(m1))==1:
     print('0'+str(m1))
else:
     print(str(m1))



