n=int(input())
s=list(input())
l='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def left(ini,cur):
     lin=abs(ini-cur)
     nlin=ini+(26-cur)
     return min(lin,nlin)

def right(ini,cur):
     lin=abs(ini-cur)
     nlin=(26-ini)+cur
     return min(lin,nlin)


A=0;C=2;T=19;G=6



res=100000
for i in range(n-3):
     count=0
     a=l.index(s[i])
     c=l.index(s[i+1])
     t=l.index(s[i+2])
     g=l.index(s[i+3])

     if A<=a:count+=left(A,a)
     else:count+=right(A,a)
     if C<=c:count+=left(C,c)
     else:count+=right(C,c)
     if T<=t:count+=left(T,t)
     else:count+=right(T,t)
     if G<=g:count+=left(G,g)
     else:count+=right(G,g)

     res=min(res,count)
print(res)
