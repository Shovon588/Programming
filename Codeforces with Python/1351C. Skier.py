t=int(input())
for _ in range(t):
  s=input()
  l=len(s)
  visited=set()
  x,y=0,0
  ans=0
  for i in range(l):
    if s[i]=='N':
      nx=x+0
      ny=y+1
    elif s[i]=='E':
      nx=x+1
      ny=y+0
    elif s[i]=='S':
      nx=x+0
      ny=y-1
    elif s[i]=='W':
      nx=x-1
      ny=y+0
    if (x,y,nx,ny) in visited or (nx,ny,x,y) in visited:
      ans+=1
    else:
      ans+=5
    visited.add((x,y,nx,ny))
    visited.add((nx,ny,x,y))
    x,y=nx,ny
  print(ans)
