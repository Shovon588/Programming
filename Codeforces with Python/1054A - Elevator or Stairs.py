x,y,z,t1,t2,t3=map(int,input().split())

stairs=abs(x-y)*t1

elevator=(abs(z-x)*t2)+(3*t3)+abs(x-y)*t2
if elevator<=stairs:print('YES')
else:print('NO')
