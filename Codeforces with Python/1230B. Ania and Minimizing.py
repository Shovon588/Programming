n,k=map(int,input().split())
s=list(input())


if n==1 and k>=1:print(0)
elif n==1 and k==0:print(''.join(s))
else:
    if s[0]!='1'  and k>0:
        s[0]='1';k-=1
        
    for i in range(1,n):
        if k>0 and s[i]!='0':
            s[i]='0';k-=1
    print(''.join(s))
