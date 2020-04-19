n=int(input())
s=input()

eight=s.count('8')

if eight==0:
     print('No')
else:
     for i in range(n-1,-1,-1):
          if s[i]=='8':
               temp=i+1
               break

     print(temp)

     if temp//2>eight-1:
          print('No')
     else:
          print('Yes')
