s=input()

l=0;r=len(s)-1
a=list(s)
b=[]

flag=[]
def permute(a,l,r):
    if l==r:
        print(a)
        print(''.join(a),end=' ')
        flag.append(''.join(a))
    else:
        for i in range(l,r+1):
            a[l],a[i]=a[i],a[l]
            permute(a,l+1,r)
            a[l],a[i]=a[i],a[l]
            
ans=permute(a,l,r)
print(len(flag))
