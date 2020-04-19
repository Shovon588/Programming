inval='DNW'
val='0123456O'
for i in range(int(input())):
    s=input();count=0
    for j in s:
        if (j not in inval) and (j in val):
            count+=1
            
    over=count//6
    ball=count%6


    if count>=6 and count%6==0:
        print(over,'OVER')
    elif count>=6 and count%6!=0:
        print(over,'OVER',ball,'BALLS')
    elif count==1:
        print(1,'BALL')
    else:
        print(ball,'BALLS')
