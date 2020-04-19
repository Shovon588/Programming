n=int(input())
a=list(input())

flag=['R','G','B']

count=0
for i in range(n-1):
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

        a[i+1]=flag[0]
        count+=1

        flag=['R','G','B']
        
print(count)
print(''.join(a))
