pos =['x++','++x','X++','++X']
neg =['x--','--x','X--','--X']
count=0

for i in range (int (input())):
    n=input()

    if n in (pos):
        count=count+1
    elif n in (neg):
        count=count-1
print (count)




        
    
