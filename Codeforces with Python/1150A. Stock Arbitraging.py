n,m,r=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

mina=min(a)
maxb=max(b)

if mina<maxb:
     temp=r//mina
     print((temp*maxb)+(r%mina))
else:
     print(r)
