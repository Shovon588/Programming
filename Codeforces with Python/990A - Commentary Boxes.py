n,m,a,b = map(int,input().split())

import math
if n%m==0:
    print(0)
elif m>n:
    des = n*b
    build = (m-n)*a
    if build<=des:
        print(build)
    else:
        print(des)
else:
    temp = math.floor(n/m)
    build = (((temp+1)*m)-n)*a
    des = (n-(temp*m))*b

    if build<=des:
        print(build)
    else:
        print(des)
