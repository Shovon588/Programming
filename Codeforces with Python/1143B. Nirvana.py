n=input()
m=''

for i in n:
     if i!='0':m+=i
     else:break

m=m+((len(n)-len(m))*'0')



n=int(m)

if len(str(n))==1:pass
elif n%10==8 or n%10==9:pass
else:n=n-(n%10)-1

n=str(n)
mul=1
for i in n:
     mul*=int(i)
print(mul)
