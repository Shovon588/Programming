from math import sqrt


def check_if_possible(num):
    temp = (n*num)-num
    temp = y-temp

    if temp<=x:
        return True
    return False


for I in range(int(input())):
    n,x,y = map(int,input().split())

    
    diff = y-x

    divisors = []
    for num in range(1,int(sqrt(diff))+2):
        if diff%num==0:
            if num not in divisors:
                divisors.append(num)
            temp = diff//num
            if temp not in divisors:
                divisors.append(temp)
    divisors.sort()

    gap = -1
    for num in divisors:
        if check_if_possible(num):
            gap = num
            break


    startwith = y
    while startwith>0 and n>0:
        print(startwith,end=' ')
        startwith-=gap
        n-=1

    for i in range(n):
        y+=gap
        print(y,end=' ')

    print()










        


    
