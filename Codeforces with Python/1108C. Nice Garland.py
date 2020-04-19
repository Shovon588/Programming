n=int(input())
a=input()
#s=list(s)

flag=['R','G','B']

count=0;res='';i=0

while i<n-1:
    l='';r=''

    if a[i]==a[i+1]:
        if i+2<n:
            r=a[i+2]
            l=a[i]
        else:
            l=a[i]
        
        if l==r or r=='':
            flag.remove(l)
        else:
            flag.remove(l)
            flag.remove(r)
            
        count+=1
        res+=a[i]
        res+=flag[0]
        i+=2
        flag=['R','G','B']
    else:
        res+=a[i]
        i+=1

if len(res)!=n:
    res+=a[-1]

print(count)
print(res)
