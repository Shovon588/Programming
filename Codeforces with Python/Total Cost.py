p,s,t,h,x=map(int,input().split())

result=0
if s-x<=t:
    result+=(s-t)*p
    result+=(x-(s-t))*h
else:
    result+=p*x

print(result)
