a,b = map(int,input().split())
from math import log
x,y = b*log(a), a*log(b)
print ('>' if x>y else '<' if y>x else '=')
