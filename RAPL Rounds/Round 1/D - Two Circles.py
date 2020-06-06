from math import sqrt

def circle(x1,y1,r1,x2,y2,r2): 
    dist = sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
    radSum = r1+r2
    
    if x1==x2 and y1==y2 and r1==r2:
        return -1
    elif (dist == radSum): 
        return 1
    elif (dist > radSum): 
        return 0
    else: 
        return 2


x1,y1,r1,x2,y2,r2 = map(int,input().split())

res = circle(x1,y1,r1,x2,y2,r2)

print(res)
