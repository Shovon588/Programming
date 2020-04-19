n=int(input())
n=str(n)
n=n[::-1]

i=0;a=''
while(i+3<=len(n)):
    a+=n[i:i+3]+','
    i+=3
    
a+=n[i:]
a=a[::-1]

if a[0]==',':
    print(a[1:])
else:
    print(a)
