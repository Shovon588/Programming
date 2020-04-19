n=int(input())
a=list(map(int,input().split()))
a.sort()

inc=[];dec=[]

flag='yes'
for i in a:
     if len(inc)==0:
          inc.append(i)
     else:
          if inc[-1]==i:
               if len(dec)==0:
                    dec.append(i)
               elif dec[-1]==i:
                    print('No')
                    flag='no'
                    break
               else:
                    dec.append(i)
          else:
               inc.append(i)
dec.sort(reverse=True)
if flag=='yes':
     print('Yes')
     print(len(inc))
     print(*inc)
     print(len(dec))
     print(*dec)
