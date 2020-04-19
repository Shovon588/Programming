n=int(input())
a=list(map(int,input().split()))

one=a.count(1)
two=a.count(2)

if one>=1 and two>=2:
     print('2 1 2',end='')
     print(' 2'*(two-2),end='')
     print(' 1'*(one-1),end='')
elif one>=1 and two==1:
     print('2 1',end='')
     print(' 1'*(one-1))
else:
     print(*a)
     
