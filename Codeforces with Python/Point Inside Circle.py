from math import sqrt as s
t=int(input())
for i in range(t):
    cx,cy,r,px,py=map(int,input().split())
    d,r=pow(cx-px,2)+pow(cy-py,2),pow(r,2)
    print('Case ',i+1,sep='',end='')
    if d<r:print(': yes')
    else:print(': no')
