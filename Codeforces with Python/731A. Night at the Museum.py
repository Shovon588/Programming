s=input()
check='abcdefghijklmnopqrstuvwxyz'
def left(ini,cur):
     lin=abs(ini-cur)
     nlin=ini+(26-cur)
     return min(lin,nlin)

def right(ini,cur):
     lin=abs(ini-cur)
     nlin=(26-ini)+cur
     return min(lin,nlin)

ini=0;res=0
for i in s:
     cur=check.index(i)
     if ini<=cur:
          res+=left(ini,cur)
     else:
          res+=right(ini,cur)
     ini=cur
print(res)
